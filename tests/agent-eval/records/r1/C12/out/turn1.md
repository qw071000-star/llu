[TOOL] list_folders(project_id=prj-sim-0001)
[TOOL] list_project_assets(folder_id=fld-3-2)

- **판단:** 3-2 컷 세션. 3-1 영상 OK(`job-v-3-1`)에서 모션만 가져와 3-2 영상 프롬프트를 씁니다. 생성은 하지 않습니다.
- **읽은 것:** 3-2 컷 카드, 정본의 3-2 줄·에셋·폴더, 3-2 마지막 핸드오프, OK 대장 「3-1 영상」·「3-2 시작 이미지」 카드, Higgsfield 3-2 폴더(`3-2 [진행]`, 검토 대기 0, 승인 `job-ff-3-2`, 거절 1).
- **지금 할 일:** 남은 빈칸 5개를 확인한 뒤 프롬프트 전문과 위험 목록을 보이겠습니다.

**3-1 영상에서 가져오는 것 (글자 그대로)**
- `ACTION_TIMING` 3줄, `PHYSICS` 4줄, 속도 문장 `All movement is slow and even; nothing accelerates suddenly.`
  - 3-1 OK 이유인 "손녀 돌아서는 속도"(0:03–0:05, 눈→머리→어깨, 약 1.5초)가 이 안에 있습니다.
- 바꾼 단어: 없음. 인물(GIRL·GRANDPA), 소품(가방·걸쇠·시간표), 구간(0:00–0:03 / 0:03–0:05 / 0:05–0:08), 길이 8초가 3-1과 같습니다.
- 카메라·렌즈는 가져오지 않습니다. 3-2 카드 값(벤치 가운데 맞은편, 앉은 눈높이, 북쪽, 고정, 대각 35°)을 씁니다.
- 컷 카드에 기록했습니다: [5] 끝·동선·시선, [6] 타이밍, [7] 가져온 OK.

**기본값으로 씀:** Seedance 2.5 · 480p(확인용) · 8초 · 16:9 · 소리 켬(대사) · 시작 이미지 `job-ff-3-2` · 참조 순서 ff_3-2_v1(시작 이미지) / char_grandpa_autumn_v1 / char_girl_raincoat_v1 / prop_doctor_bag_v1 · 저장 `fld-3-2`

**프롬프트를 쓰기 전에 확인할 것이 5개 있습니다. 제안값이 괜찮으면 "그대로", 바꿀 것만 답해 주세요.**

[렌즈]
1. 관찰 결과·초점: 제안 — 벤치와 시간표가 나란히 화면을 채움 / 뒤 논은 압축되고 흐림 / 얼굴·몸에 광각 왜곡 없음. 초점은 두 사람에 고정, 초점 이동 없음.
   (이유: 승인된 시작 이미지 `job-ff-3-2`의 화면 그대로)

[인물]
2. 연기: 제안 — 3-1 영상의 연기 문장 그대로. 손녀는 할아버지가 정해 주길 바람(걱정 ~ 조바심). 할아버지는 예상했다는 걸 숨김(정지 ~ 조용한 체념), 손녀를 보지 않음. 둘 다 카메라를 보지 않음.
   (이유: 3-1과 섞어 편집하므로 연기가 같아야 튀지 않음)
   - 선택: 눈의 삶 문장 한 줄 추가. 3-2는 얼굴이 커서 죽은 눈이 잘 보입니다.
3. 손녀가 들어가지 않는 구역: 제안 — 길(전경). 시간표와 벤치 사이에만 머묾.
   (이유: 3-1과 같은 동선)

[소리·이음새]
4. 소리: 제안 — 3-1과 같게. 손녀 "할아버지, 막차 갔대." 한 번(0:03–0:05), 할아버지는 말도 입 움직임도 없음, 먼 논 위 바람 소리, 음악 없음.
   (이유: 섞어 편집할 때 대사·바람 소리가 이어져야 함)
5. 다음 컷 첫 프레임과 맞출 것: 제안 — 따로 맞추지 않고 끝 상태를 3-1과 같게 둠(손녀 벤치 쪽, 할아버지 가방 봄).
   (이유: 3-2는 3-1과 섞어 쓰므로 3-1과 같은 끝에서 3-3으로 넘어감)

=== 메타 ===
- 연 파일(순서대로):
  1. PLAYER-RULES.md
  2. SKILLS-INDEX.md · CLAUDE.md · .claude/instructions.md (동시에 열었음)
  3. .claude/skills/production-session/SKILL.md
  4. .claude/skills/production-session/ok-reuse.md
  5. project/decisions.md · project/shot-list.md · project/asset-registry.md (한 번에 열었음. shot-list·asset-registry는 파일 전체가 출력됐고 3-2 줄, 이음새 표, CH-001·CH-002·PR-001·LC-001, 폴더 표만 사용)
  6. project/cuts/3-2.md
  7. project/log/3-2_handoff_2026-10-27.md
  8. project/ok-cuts.md — 제목 목록(grep), 목록 표(1–27행), 「3-1 영상」·「3-2 시작 이미지」 절(278–390행)만
  9. .claude/skills/video-prompt/SKILL.md
  10. .claude/skills/video-prompt/live-action.md
  11. sim/higgsfield.md
  12. .claude/skills/acting/SKILL.md
- 부른 [TOOL]:
  - list_folders(project_id=prj-sim-0001) → 3-2 [진행] `fld-3-2`
  - list_project_assets(folder_id=fld-3-2) → 검토 대기 0, 승인 `job-ff-3-2`, 거절 1(`job-ff-3-2-old`)
- 고친 정본 파일:
  - project/cuts/3-2.md — [5] 끝(마지막 프레임)·동선·시선, [6] 타이밍, [7] 가져온 OK (3-1 영상 모션에서 채움. 지나가지 않는 구역·대사 원문·다음 컷 맞춤·렌즈 관찰 결과는 질문 중이라 [ ]로 둠)
