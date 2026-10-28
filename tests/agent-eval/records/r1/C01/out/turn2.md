[TOOL] create_project(workspace_id: "ws-sim-0001", name: "빈 정류장")
[TOOL] create_folder(project_id: "prj-new-0001", name: "00 에셋")
[TOOL] create_folder(project_id: "prj-new-0001", parent_id: "fld-00 에셋", name: "인물")
[TOOL] create_folder(project_id: "prj-new-0001", parent_id: "fld-00 에셋", name: "장소")
[TOOL] create_folder(project_id: "prj-new-0001", parent_id: "fld-00 에셋", name: "소품")
[TOOL] create_folder(project_id: "prj-new-0001", parent_id: "fld-00 에셋", name: "그림체")
[TOOL] create_folder(project_id: "prj-new-0001", name: "99 시험·보관")

정본 초안을 쓰고 Higgsfield 프로젝트와 폴더를 만들었습니다.

**만든 것**
- 프로젝트: 「빈 정류장」 `prj-new-0001` (팀 워크스페이스)
- 폴더: `00 에셋`(`fld-00 에셋`) 아래 인물 `fld-인물` · 장소 `fld-장소` · 소품 `fld-소품` · 그림체 `fld-그림체`, `99 시험·보관`(`fld-99 시험·보관`)
- 정본(`project/`):
  - `decisions.md`: 형식·모델·룩·카메라·금지 요소·작업 방식, 미결 2건
  - `asset-registry.md`: 폴더 ID, CH-001 할아버지 · CH-002 손녀 · LC-001 시골 버스 정류장(ID만)
  - `shot-list.md`·`ok-cuts.md`: 제목만 넣고 빈 표로 둠

**정한 것**
- 장면 3개(말씀하신 값)
- 나머지는 기본값: 16:9 · 전체 3분 · 컷당 8초(약 22컷) · 실사
- 모델: GPT Image 2.5 / Seedance 2.5(인물 컷) · Kling 4.0(배경 컷)
- 해상도: 확인 1k·480p, 확정 2k·1080p · 소리 끔(대사 컷만 켬)
- 현재 한국 시골, 밤 · 고정·아이레벨 · 글자 금지 · 편집·색 보정 가능

**아직 비어 있는 것(미결)**
- 시나리오가 없어 컷 목록이 빈 표입니다. 장면 3개의 내용이 정해져야 컷을 나눌 수 있습니다.
- 막차 버스가 화면에 나오는지 정하지 않아 소품 ID를 보류했습니다.

**한 번만 부탁드립니다:** `.claude/instructions.md` 맨 위 "이 프로젝트"에 아래 세 가지를 넣어 주세요. 다음 대화부터 바로 시작할 수 있습니다.
- 작품: 「빈 정류장」(가제)
- Higgsfield 프로젝트: 빈 정류장 (`prj-new-0001`)
- 정본 위치: 리포 `project/`

**다음 순서** (실사라 그림체 기준 이미지는 건너뜁니다)
1. 인물+의상 시트: CH-001 할아버지, CH-002 손녀
2. 장소 마스터: LC-001 시골 버스 정류장(밤)
3. 소품 에셋(시나리오가 정해진 뒤)
4. 컷 카드를 발행하고 컷 세션을 엽니다.

**질문**
1. 시나리오: 장면 3개의 내용을 주시겠어요, 아니면 제가 3분 구성안(장면별 한 줄과 컷 나눔)을 드릴까요?
2. "이 프로젝트" 세 줄을 제가 넣을까요, 직접 넣으시겠어요?

=== 메타 ===
- 연 파일(순서대로):
  - 새로 연 파일 없음. project-setup SKILL.md, higgsfield-generation SKILL.md §2, sim/higgsfield.md(create_project·create_folder 결과), 정본 4개는 1턴에서 읽은 내용으로 처리했다.
- 부른 [TOOL]:
  1. create_project(workspace_id: "ws-sim-0001", name: "빈 정류장") → `prj-new-0001`
  2. create_folder(project_id: "prj-new-0001", name: "00 에셋") → `fld-00 에셋`
  3. create_folder(… parent_id: "fld-00 에셋", name: "인물") → `fld-인물`
  4. create_folder(… parent_id: "fld-00 에셋", name: "장소") → `fld-장소`
  5. create_folder(… parent_id: "fld-00 에셋", name: "소품") → `fld-소품`
  6. create_folder(… parent_id: "fld-00 에셋", name: "그림체") → `fld-그림체`
  7. create_folder(project_id: "prj-new-0001", name: "99 시험·보관") → `fld-99 시험·보관`
- 고친 정본 파일:
  - project/decisions.md: 제목, §1, §2, §3, §4, §7, §8, 미결 표
  - project/asset-registry.md: 제목, 폴더 표, CH-001 할아버지 이름, CH-002 손녀 절 추가, LC-001 장소명
  - project/shot-list.md: 제목 줄만
  - project/ok-cuts.md: 제목 줄만
