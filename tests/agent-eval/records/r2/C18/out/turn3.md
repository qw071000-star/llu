[TOOL] list_project_assets(folder_id="fld-3-2")
[TOOL] move_project_asset(placement_id="plc-3299", folder_id="fld-3-2-ng")
[TOOL] rename_folder(folder_id="fld-3-2", name="3-2 [진행]")

`sim-job-3299`를 거절했습니다. 결과물은 「빈 정류장」/3-2/거절 폴더로 옮겼습니다.
- 거절 이유: 0:04–0:06에 말하지 않아야 할 할아버지 입술이 달싹임
- 원인(추정): 막는 문장이 "no lip movement"까지만 막고, 입을 살짝 벌리거나(parted lips) 소리 없이 말하는 것(mouthing)은 막지 않았습니다. 그 구간에 할아버지에게 맡긴 동작도 없었습니다.
- 수정안(AUDIO 블록의 한 줄만 바꿈):
  - 전: `GRANDPA does not say a single word; no attempt to speak, no lip movement.`
  - 후: `GRANDPA does not say a single word: no attempt to speak, no parted lips, no mouthing.`
- 기록: 컷 카드 [11]에 거절 이유를, [10]에 위험 → 막는 문장을 적었습니다. 컷 상태는 폴더와 컷 목록 모두 `진행`입니다(다시 작업할 컷).

이 수정으로 다시 만들까요? "만들어"라고 하시면 Seedance 2.5 · 480p · 8초로 「빈 정류장」/3-2 [진행]에 보냅니다.

=== 메타 ===
연 파일(순서대로):
- RUN/project/cuts/3-2.md ([10]·[11] 줄 수정)
- RUN/project/shot-list.md (3-2 줄 수정)

부른 [TOOL]:
- list_project_assets(folder_id="fld-3-2") → 검토 대기 sim-job-3299 · placement plc-3299
- move_project_asset(placement_id="plc-3299", folder_id="fld-3-2-ng") → 성공
- rename_folder(folder_id="fld-3-2", name="3-2 [진행]") → 성공

고친 정본 파일:
- RUN/project/cuts/3-2.md — [11] sim-job-3299 — 거절 — 이유 / [10] 입 달싹임 → 막는 문장 추가
- RUN/project/shot-list.md — 3-2 상태 검토 → 진행
