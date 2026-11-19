# Several Higgsfield accounts

Applies when `decisions.md` §7 lists several Higgsfield accounts (e.g. `A 공용 · B~E 개인`) used from one Claude account. The Higgsfield connector holds one login at a time. A shared account among them also follows `shared-account.md`.

1. **Which account.** At session start ask "어느 계정(A~E)으로 작업하나요?" once. Find its workspace ID in the registry `계정` table. Before any generation, `list_workspaces` must show that workspace as selected; otherwise do not generate: ask the user to reconnect the Higgsfield connector as that account (Settings → Connectors: disconnect, connect, log in).
2. **Elements exist in every account, with the same names.** Anyone may make a new element: in the account that made the confirmed source image use its job; elsewhere import it from its original URL with `media_import_url`; create the element with `manage_reference_elements` (`create`, the registry name, description `에셋 ID · 버전 · 원본 주소`), and write the new ID in the registry `계정별 ID` table. The other accounts get it at their next session start: compare the registry with that account's element list and create every missing one from the original URL, then fill the cell. Use an element only when its status is `completed`. A discarded version is not synced.
3. **References are this account's IDs.** Element, job and media IDs differ per account; never send another account's. A result made in another account (start image, location master, sheet): import it from its original URL and use the returned media ID; add one line to the registry `가져온 이미지` table.
4. **Seedream 5.5 · Seedance 2.5:** attach this account's media IDs (imported sheet, location, start image) in `medias` and call them in attach order (`<<<image_1>>>` …), not element tags.
5. **Draft finalization:** a Seedance 2.5 draft is made 1080p only in the account that made it, within 7 days (`video-prompt` → `rerender.md`).
6. **Records:** the OK card `승인` line ends with the name and `계정: B`; the 콘티 records only the account (`production-session` → `storyboard.md`); the cut list `생성/크레딧` cell starts with the account (`B · 이미지 2 · 약 1 크레딧`). Credits are per account.

Not yet tested (say so when it matters): whether an element made from the same image behaves the same in every account, and whether creating an element costs credits.
