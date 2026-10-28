[TOOL] list_folders(project_id=prj-sim-0001)
[TOOL] list_project_assets(folder_id=fld-locs)

- 판단: 장소 에셋 LC-001의 새 뷰 요청이라 총괄 세션으로 봤습니다. LC-001-V1(길 건너에서 북쪽을 봄)의 축을 정확히 뒤집어, 정류장 안에서 남쪽(길)을 보는 DERIVED VIEW(`LC-001-V2`)입니다.
- 읽은 것: decisions·shot-list·asset-registry, OK 대장의 LC-001-V1 카드와 1-1 카드, 3-1·3-2 핸드오프(이미 반영됨), Higgsfield 폴더(장소 폴더 `fld-locs`, 검토 대기 0).
- 지금 할 일: 아래 빈칸 5개가 정해지면 위험 목록과 프롬프트를 먼저 보여 드립니다. 생성은 지시하실 때 1k 한 장으로 보냅니다.

**정본에서 채운 것** (바꿀 것만 말씀해 주세요)
- 모드: DERIVED VIEW(새 시점, V1 카메라를 물려받지 않음) + 반대 방향 문장(`not a horizontal mirror of the reference`)
- 형식: GPT Image 2.5 · 1k 확인 · 16:9 · 1장
- 참조: 1장, `job-lc001v1`(LC-001-V1) = 같은 장소(지리·재질·랜드마크·빛 방향)
- 카메라 높이: 아이레벨(선 눈높이), 삼각대 고정 (확정 사항 §4)
- 고정문: MASTER GEOMETRY · LIGHT LOCK · Nothing else는 에셋 대장에서 글자 그대로, 팔레트·재질·마감·시대는 V1 카드에서 그대로
- 화면 대응: 남쪽을 보므로 **서(감나무·해) = 화면 오른쪽, 동(시간표) = 화면 왼쪽**. V1과 좌우가 반대입니다.
- 길 건너편: 그루터기가 남은 추수한 논 (1-1 OK `job-ff-1-1`)
- 저장: 00 에셋 / 장소 `fld-locs` (에셋 대장 폴더 표)
- 확정되면: `LC-001-V2` · 요소 이름 `loc_busstop_inside_v1`(이름 규칙에 맞춘 제안)

프롬프트를 쓰기 전에 확인할 것이 5개 있습니다. 제안값이 괜찮으면 "그대로"라고 해 주세요.
1. 카메라 위치(정류장 안 어디): 제안 — 뒷벽 벤치 가운데 바로 앞 (이유: 앞 개구부 전체가 액자로 잡히고 V1 카메라와 정확히 마주 봄)
2. 방향·샷 크기: 제안 — 정남쪽 정면, 와이드. 2차선 길이 화면을 좌우로 가로지름 (이유: "길 쪽"을 그대로 뒤집은 축. 3-6처럼 길 끝에서 오는 버스를 담을 뷰라면 축이 달라지니 동·서 중 어느 쪽으로 틀지 알려 주세요)
3. 처음 보이는 지배 요소: 제안 — 앞 개구부(함석지붕 처마와 양쪽 벽 끝)가 액자처럼 감싼 빈 길, 그 위로 화면 오른쪽(서)에서 낮게 드는 노을빛 (이유: 안에서 밖을 보는 뷰의 핵심이고, V1과 같은 빛 논리)
4. 길 건너 먼 배경(남쪽 지평선): 제안 — 논이 평평하게 이어지다 멀리 낮은 산줄기 (이유: 길 남쪽 논까지는 1-1에 있지만 그 너머는 정본에 없음. 북쪽과 같은 지형으로 맞춤)
5. 남길 랜드마크 / 뺄 것: 제안 — 남김: 개구부 액자, 화면 왼쪽 벽 밖 시간표 기둥(뒷면만), 화면 오른쪽 끝 감나무 가지 / 뺌: 벤치·뒷벽(카메라 뒤), 북쪽 논·산 (이유: 랜드마크 1~3개 규칙. 시간표 글씨 면은 길 쪽을 향한다고 추정하므로 안쪽에서는 뒷면이 되어 글자 위험도 줄어듦)

=== 메타 ===
연 파일(순서대로):
1. RUN/PLAYER-RULES.md
2. RUN/CLAUDE.md
3. RUN/.claude/instructions.md
4. RUN/SKILLS-INDEX.md
5. RUN/project/decisions.md
6. RUN/project/asset-registry.md
7. RUN/project/shot-list.md
8. RUN/.claude/skills/production-session/SKILL.md
9. RUN/.claude/skills/image-prompt/SKILL.md
10. RUN/.claude/skills/image-prompt/location.md
11. RUN/.claude/skills/higgsfield-generation/SKILL.md
12. RUN/sim/higgsfield.md
13. RUN/project/ok-cuts.md — 제목 목록(grep), 목록 절(1–27행), `### LC-001-V1 장소` 절(90–114행)만
14. RUN/project/log/3-1_handoff_2026-10-26.md
15. RUN/project/log/3-2_handoff_2026-10-27.md
16. RUN/project/ 전체 키워드 검색(grep: 반대|길 쪽|south|남쪽|reverse|V2|안에서) — 걸린 곳은 ok-cuts.md 23행·128행뿐, 컷 카드 본문은 열지 않음
17. RUN/project/ok-cuts.md — `### 1-1 시작 이미지` 절(115–138행)만 (길 남쪽 지형 확인용)

부른 [TOOL]:
- list_folders(project_id=prj-sim-0001) → 00 에셋 / 장소 `fld-locs` 있음
- list_project_assets(folder_id=fld-locs) → 검토 대기 0 · 승인 0 · 거절 0 (반대 뷰 시도 없음)

고친 정본 파일: 없음 (빈칸 답을 받은 뒤 에셋 대장 LC-001 뷰 표에 기록할 예정)
