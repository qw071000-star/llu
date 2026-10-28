[TOOL] list_project_assets(folder_id: "fld-3-2")
[TOOL] move_project_asset(placement_id: "plc-3201", to_folder_id: "fld-3-2-ok")
[TOOL] rename_folder(folder_id: "fld-3-2", name: "3-2 [승인]")

승인 처리했습니다. 3-2 영상 `sim-job-3201`.
- 결과물을 `3-2 / 승인` 폴더로 옮기고, 컷 폴더를 `3-2 [승인]`으로 바꿨습니다. 컷 목록 상태도 `승인`, 확정 영상 job은 `sim-job-3201`로 적었습니다.
- OK 대장에 3-2 영상 카드를 추가했습니다: 설정(Seedance 2.5 · 480p · 8초 · 16:9 · 소리 켬), 참조 4개와 순서, 3-1 영상에서 가져온 모션(ACTION_TIMING, PHYSICS), OK 이유 "좋아, 3-2 영상 OK", 위험 → 막는 문장, 보낸 프롬프트 글자 그대로.
- 시드는 알 수 없어 그렇게 적었습니다.
- 3-1과 3-2는 같은 동작·타이밍이라 편집에서 섞어 쓰실 수 있습니다.

=== 메타 ===
연 파일(순서대로): project/ok-cuts.md(목록, 3-1·3-2 카드 형식), project/shot-list.md, project/cuts/3-2.md, tmp/p32.txt(보낸 프롬프트), higgsfield-generation/check_prompt.py(재검사 통과)
부른 [TOOL]: list_project_assets(fld-3-2) · move_project_asset(plc-3201 -> fld-3-2-ok) · rename_folder(fld-3-2 -> 3-2 [승인])
고친 정본 파일: project/ok-cuts.md(목록 줄 + 3-2 영상 카드), project/shot-list.md(3-2 상태 승인, 확정 영상 sim-job-3201), project/cuts/3-2.md([11] 승인 기록, [12])
