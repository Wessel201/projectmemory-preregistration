"""Plan 23 amendment 1, Step 0: check the quotes and code references of the design register.

Reads `23-am1-register-design-and-controls.md` and checks, with no model, network or app import:

1. Design quotes. A quote governed by a paragraph id (`**D4.p3**`, `D4.p3:`, `T.rationale`) must be
   a substring of that paragraph in `23-am1-design-text-94c049d.md`. Each paragraph of that file is
   first compared with its line range in `git show 94c049d:thesis/implementation_chapter.tex`.
2. Commit quotes. A quote governed by `commit:path:a-b` must be a substring of lines a-b of
   `git show commit:path`. Quotes from 3320375 are the code and note quotes of that commit.
3. Amendment and other working-tree quotes. A quote governed by `path:a-b` (no commit) of a file
   outside `app/` must be a substring of lines a-b of the working-tree file.
4. Code quotes in the implementation format (`path:line` or `l.N`, no commit, under `app/`). These
   cite lines relative to a file named earlier, so they are checked at file level: the quote must
   occur in a file of 3320375 named in the register (also after joining adjacent Python string
   literals, or comment lines), or in `23-am1-prompts-evaluated.md`. A quote with no cited source
   may also be a section title or label of the amendment, the loss-trace codebook or the register
   itself, or a string of the trace of a run named on its line (a0_r1 ... a2_r3). Fenced code
   blocks introduced as verbatim are checked against 3320375, within their cited line range.
5. Code references `name` (`3320375:path:line`): the name occurs on that line at 3320375.
6. Direction: a quote cited to a later commit of the chapter (a retrospective entry) must not occur
   in the 94c049d chapter; a `before` quote from 94c049d is reported if it still occurs at b4d6b6c.
   These are reported as notes, not errors; the register lists its known exceptions.

Governing source: a cited source written right after the quote, as `"..." (`path:N`)`; otherwise
the last paragraph id or cited source that precedes the quote on its line.
Normalisation: every run of whitespace becomes one space (the register joins LaTeX line breaks
with one space; nothing else is changed). A quote of fewer than 12 characters with no governing
source is skipped (single words in glosses). Straight double quotes delimit quotes; quotes inside
backtick code spans are not quotes.

Usage: .venv/bin/python thesis/notes/thesis_completion/artifacts/23-am1-check-register.py [--verbose] [REGISTER]
REGISTER defaults to the register next to this script (another path is for testing the checker).
Exit status 0 when checks 1-5 pass, 1 otherwise. Prints counts per check and every failure;
--verbose also lists where each quote of check 4 was found and each skipped quote.
"""

import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
REGISTER = HERE / "23-am1-register-design-and-controls.md"
DESIGN = HERE / "23-am1-design-text-94c049d.md"
PROMPTS = HERE / "23-am1-prompts-evaluated.md"
CHAPTER = "thesis/implementation_chapter.tex"
CODE_COMMIT = "3320375"
AMENDMENT = HERE / "23-plan-amendment-1-ceilings-and-root-cause.md"
LOSS_CODEBOOK = HERE / "23-loss-trace.md"
RUNS = ROOT / "data/ami_eval/a1_smoke"
RUN_RE = re.compile(r"\b(a[012]_r[123]b?)\b")
MIN_UNSOURCED = 12

ID_RE = re.compile(r"\*\*(D\d+\.p\d+|T\.rationale)\*\*|\b(D\d+\.p\d+|T\.rationale)(?=:\s)")
SRC_RE = re.compile(r"^(?:([0-9a-f]{7,40}):)?([\w./-]+\.(?:py|md|tex|yaml|json|sh)):(\d+)(?:-(\d+))?$")
CODEREF_RE = re.compile(r"`([^`]+)` \(`" + CODE_COMMIT + r":([^`:]+):(\d+)`\)")
FILE_RE = re.compile(r"\b((?:app|scripts)/[\w/]+\.py)\b")
LINES_RE = re.compile(r"(?:l\.|:)(\d+)-(\d+)")

_git_cache = {}


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


def git_show(commit, path):
    key = (commit, path)
    if key not in _git_cache:
        r = subprocess.run(["git", "show", f"{commit}:{path}"], cwd=ROOT, capture_output=True, text=True)
        _git_cache[key] = r.stdout.split("\n") if r.returncode == 0 else None
    return _git_cache[key]


def join_literals(text):
    """Join adjacent Python string literals ("a" "b" -> "ab") so prompt sentences split in code match."""
    return re.sub(r"(?<!\\)[\"']\s*\n?\s*f?[\"']", "", text)


def join_comments(text):
    """Join consecutive comment lines (# a / # b -> a b) so a comment quoted across a break matches."""
    return re.sub(r"\n\s*#\s?", " ", text)


def design_paragraphs():
    """Paragraph id -> normalised text, after checking each paragraph against git show 94c049d."""
    text = DESIGN.read_text().split("\n")
    chapter = git_show("94c049d", CHAPTER)
    paras, errors = {}, []
    i = 0
    while i < len(text):
        m = re.match(r"\*\*(D\d+\.p\d+|T\.rationale)\*\* \(lines (\d+)-(\d+)\)", text[i])
        if m:
            start = text.index("```latex", i) + 1
            stop = text.index("```", start)
            body = text[start:stop]
            pid, a, b = m.group(1), int(m.group(2)), int(m.group(3))
            if body != chapter[a - 1 : b]:
                errors.append(f"design-text {pid}: lines {a}-{b} differ from git show 94c049d")
            paras[pid] = norm(" ".join(body))
            i = stop
        i += 1
    return paras, errors


def scan(line):
    """Yield ('tok', value) for ids and backtick spans, and ('quote', text, col) for quotes, in order."""
    i, n = 0, len(line)
    while i < n:
        c = line[i]
        if c == "`" and not line.startswith("``", i):
            j = line.find("`", i + 1)
            if j < 0:
                return
            yield ("code", line[i + 1 : j])
            i = j + 1
        elif c == '"':
            j, buf = i + 1, []
            while j < n and line[j] != '"':
                if line.startswith("\\\\", j):  # a LaTeX \\ before a closing quote
                    buf.append("\\\\")
                    j += 2
                    continue
                if line[j] == "\\" and j + 1 < n and line[j + 1] == '"':
                    buf.append('"')
                    j += 2
                    continue
                buf.append(line[j])
                j += 1
            if j >= n:
                yield ("open", line[i:])
                return
            yield ("quote", "".join(buf), j + 1)
            i = j + 1
        else:
            j = i
            while j < n and line[j] not in '`"':
                j += 1
            if line.startswith("``", i):
                j = i + 2
            for m in ID_RE.finditer(line[i:j]):
                yield ("id", m.group(1) or m.group(2))
            i = j


def main():
    verbose = "--verbose" in sys.argv
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    register = pathlib.Path(args[0]) if args else REGISTER
    reg = register.read_text().split("\n")
    paras, errors = design_paragraphs()
    prompts = norm(PROMPTS.read_text())
    amend_cache = {}

    code_files = sorted(set(FILE_RE.findall("\n".join(reg))))
    code_text = {}
    for p in code_files:
        src = git_show(CODE_COMMIT, p)
        if src is None:
            errors.append(f"register names {p}, which does not exist at {CODE_COMMIT}")
            continue
        whole = "\n".join(src)
        code_text[p] = (src, norm(whole), norm(join_literals(whole)), norm(join_comments(whole)))
    chap94 = norm("\n".join(git_show("94c049d", CHAPTER)))
    chapb4 = norm("\n".join(git_show("b4d6b6c", CHAPTER)))

    counts = {k: 0 for k in ("design", "commit", "worktree", "code-file", "code-block", "coderef", "skipped")}
    notes, unsourced = [], []

    def worktree_lines(path):
        if path not in amend_cache:
            f = ROOT / path
            amend_cache[path] = f.read_text().split("\n") if f.exists() else None
        return amend_cache[path]

    def check_code_file(q, where, line=""):
        nq = norm(q)
        for p, (_, *variants) in code_text.items():
            if any(nq in v for v in variants):
                return p
        if nq in prompts:
            return PROMPTS.name
        for extra in (AMENDMENT, LOSS_CODEBOOK):
            if nq in norm(extra.read_text()):
                return extra.name
        if len(nq.split()) <= 5 and nq in norm("\n".join(l for l in reg if l != line)):
            return "this register (a label of at most five words that it uses elsewhere)"
        for run in sorted(set(RUN_RE.findall(line))):
            for t in RUNS.glob(f"**/{run}/artifacts/*.trace.json"):
                if q in t.read_text() or q.replace("'", "\\u0027") in t.read_text():
                    return str(t.relative_to(ROOT))
        errors.append(f"{where}: code quote not found in any named 3320375 file or the prompt file: {q[:90]!r}")
        return None

    in_fence, fence_start, fence_intro = False, None, ""
    for ln, line in enumerate(reg, 1):
        if line.strip().startswith("```"):
            if not in_fence:
                in_fence, fence_start = True, ln
                fence_intro = next((reg[k] for k in range(ln - 2, -1, -1) if reg[k].strip()), "")
            else:
                in_fence = False
                if "erbatim" in fence_intro:
                    counts["code-block"] += 1
                    block = norm("\n".join(reg[fence_start:ln - 1]))
                    rng = LINES_RE.findall(fence_intro)
                    a, b = (int(rng[-1][0]), int(rng[-1][1])) if rng else (None, None)
                    named = [p for p in code_files if p in fence_intro or pathlib.Path(p).name in fence_intro]
                    ok = False
                    for p in named or code_files:
                        src = code_text.get(p, (None,))[0]
                        if src and block in norm("\n".join(src[a - 1 : b] if a else src)):
                            ok = True
                            break
                    if not ok:
                        errors.append(f"line {fence_start}: verbatim code block not found at {CODE_COMMIT} in its cited range")
            continue
        if in_fence:
            continue

        for name, path, num in CODEREF_RE.findall(line):
            counts["coderef"] += 1
            src = git_show(CODE_COMMIT, path)
            if src is None or int(num) > len(src) or name not in src[int(num) - 1]:
                errors.append(f"line {ln}: code reference `{name}` not on {CODE_COMMIT}:{path}:{num}")

        gov = None
        for item in scan(line):
            if item[0] == "id":
                gov = ("design", item[1])
            elif item[0] == "code":
                m = SRC_RE.match(item[1])
                if m:
                    gov = ("src", m.group(1), m.group(2), int(m.group(3)), int(m.group(4) or m.group(3)))
            elif item[0] == "open":
                errors.append(f"line {ln}: unbalanced quotation mark")
            elif item[0] == "quote":
                q, nq = item[1], norm(item[1])
                where = f"line {ln}"
                after = re.match(r"\s*\(`([^`]+)`\)", line[item[2]:])
                m = SRC_RE.match(after.group(1)) if after else None
                if m:
                    gov = ("src", m.group(1), m.group(2), int(m.group(3)), int(m.group(4) or m.group(3)))
                if gov and gov[0] == "design":
                    counts["design"] += 1
                    if gov[1] not in paras:
                        errors.append(f"{where}: unknown paragraph id {gov[1]}")
                    elif nq not in paras[gov[1]]:
                        errors.append(f"{where}: not in {gov[1]}: {q[:90]!r}")
                    continue
                if gov and gov[0] == "src":
                    _, commit, path, a, b = gov
                    if commit:
                        counts["commit"] += 1
                        src = git_show(commit, path)
                        if src is None:
                            errors.append(f"{where}: cannot read {commit}:{path}")
                        elif nq not in norm("\n".join(src[a - 1 : b])):
                            errors.append(f"{where}: not in {commit}:{path}:{a}-{b}: {q[:90]!r}")
                        if path == CHAPTER and commit != "94c049d" and nq in chap94:
                            notes.append(f"{where}: retrospective quote ({commit}) also occurs at 94c049d: {q[:70]!r}")
                        if path == CHAPTER and commit == "94c049d" and line.lstrip().startswith("- before") and nq in chapb4:
                            notes.append(f"{where}: 'before' quote still occurs at b4d6b6c: {q[:70]!r}")
                    elif path.startswith(("app/", "scripts/")) or not (ROOT / path).exists():
                        counts["code-file"] += 1
                        check_code_file(q, where, line)
                    else:
                        counts["worktree"] += 1
                        src = worktree_lines(path)
                        if nq not in norm("\n".join(src[a - 1 : b])):
                            errors.append(f"{where}: not in {path}:{a}-{b}: {q[:90]!r}")
                    continue
                if len(nq) < MIN_UNSOURCED:
                    counts["skipped"] += 1
                    if verbose:
                        unsourced.append(f"{where}: skipped short quote {q!r}")
                    continue
                counts["code-file"] += 1
                found = check_code_file(q, where, line)
                if verbose and found:
                    unsourced.append(f"{where}: located in {found}")

    print(f"design paragraphs: {len(paras)} (each compared with git show 94c049d)")
    for k, v in counts.items():
        print(f"{k}: {v}")
    print(f"errors: {len(errors)}")
    for e in errors:
        print("  ERROR", e)
    print(f"direction notes: {len(notes)}")
    for n_ in notes:
        print("  NOTE", n_)
    if verbose:
        for u in unsourced:
            print("  ", u)
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
