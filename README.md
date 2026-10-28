# llu — AI 이미지·영상 제작 지침 키트

「어머니와 고등어」(실사 단편)와 나부코 '히브리 노예들의 합창'(수채 배경 영상) 작업, 다른 작품 The Prompter 분석, Higgsfield 생성 기록 930건에서 확인된 규칙과 실수를 **어느 프로젝트에나 넣어 쓸 수 있게** 정리한 저장소다.

목표는 셋이다.
1. 새 세션마다 같은 설명을 반복하지 않는다.
2. 다른 작업에서 했던 실수를 다시 하지 않는다.
3. 크레딧과 토큰을 헛쓰지 않는다.

---

## 바로 쓰기

### Claude 앱 프로젝트(Projects)에서

1. 작품마다 프로젝트를 하나 만든다.
2. **지침 칸**에 `guide/00_project-instructions.md` 내용을 붙인다.
3. **프로젝트 지식**에 올린다: `guide/01`~`07`, `templates/`에서 쓰는 것, 그리고 작품 정본 세 개(`templates/decisions.md`·`asset-registry.md`·`shot-list.md`를 복사해 채운 것).
4. 총괄 세션과 컷 세션을 같은 프로젝트 안의 새 대화로 연다. 첫 메시지는 `templates/session-start.md`의 문구.
5. 총괄 세션에서 정본이 바뀌면 지식 파일을 교체한다.

### Claude Code(리포)에서

1. 작품 리포에 `guide/`와 `templates/`를 복사한다.
2. `templates/CLAUDE.md`를 리포 루트의 `CLAUDE.md`로 복사하고 `[작품명]`을 채운다.
3. `project/` 폴더에 정본 세 개와 `cuts/`, `log/`를 만든다.

---

## 파일 지도

| 파일 | 무엇 | 언제 읽나 |
|---|---|---|
| `guide/00_project-instructions.md` | **핵심 규칙 12개 + 문서 지도.** 지침 칸에 붙이는 판 | 항상(자동) |
| `guide/01_work-rules.md` | 사용자 말 해석표, 생성 전 4단계, 보고 형식, 고칠 때 규칙 | 생성·수정할 때 |
| `guide/02_session-system.md` | 총괄 세션 + 컷 세션, 문서 층, 패킷, 토큰 절약, 설치법 | 세션을 열고 닫을 때 |
| `guide/03_video-prompt.md` | 영상: 샷 설계, 15블록, 4문단, 검증된 문장, 실패→수정 표 | 영상 프롬프트 |
| `guide/04_image-prompt.md` | 이미지: 모드 판별, 참조 권한, 인물 시트, 장소, 소품, 그림체, 크롭, 퍼스트 프레임 | 이미지 프롬프트 |
| `guide/05_acting.md` | 연기: 목표·비즈니스·눈·상태·마스터 프로필·검증 문장 | 인물이 나오는 영상 |
| `guide/06_qa-and-cost.md` | 확인→확정 파이프라인, 검수 지표, 재시도 한도, 후반으로 넘길 것, 실제 크레딧 통계·단가 | 검수, 해상도 결정 |
| `guide/07_error-registry.md` | **오류 대장 45건**(무슨 일·원인·지금 규칙·출처) | 새 작업 시작 전, 실수가 났을 때 |
| `templates/decisions.md` | 확정 사항 틀 + 시작 전에 물어볼 12가지 | 작품 시작 |
| `templates/asset-registry.md` | 에셋 대장 틀(인물·장소·소품·그림체, 고정 설명문) | 에셋 확정 |
| `templates/shot-list.md` | 컷 목록·이음새·소품 연속성 표 | 총괄 |
| `templates/cut-card.md` | 총괄 → 컷 세션 패킷 | 컷 작업 시작 |
| `templates/handoff.md` | 컷 세션 → 총괄 보고 | 컷 작업 끝 |
| `templates/session-start.md` | 새 대화 첫 메시지 문구 | 세션 시작 |
| `templates/video-prompt.md` | 영상 프롬프트 빈 틀(15블록·짧은 판·4문단·재렌더) | 영상 프롬프트 |
| `templates/image-prompts.md` | 이미지 프롬프트 빈 틀 8종 | 이미지 프롬프트 |
| `templates/CLAUDE.md` | Claude Code 리포용 | 리포 설정 |
| `analysis/higgsfield-history.md` | Higgsfield 전 프로젝트 분석: 잘된 것·안 된 것·크레딧 | 참고 |
| `analysis/source-index.md` | 원본 자료 색인(이 리포 루트 파일, Docs 문서 8개, Higgsfield 프로젝트) | 근거 확인 |

루트의 한국어 파일들(`확정 사항 — …`, `production-os-prompt-guide.md`, `acting-guide.md`, `location-*.md`, `00.`~`12.` 등)은 「어머니와 고등어」의 **원본 지침**이다. 그 작품을 이어서 할 때는 원본을, 다른 작품에는 `guide/`를 쓴다.

---

## 키트를 고칠 때

- 새 실수 → `guide/07_error-registry.md` 맨 아래에 `E-46`부터 추가하고, 관련 가이드에 한 줄로 가리킨다.
- 새로 효과가 확인된 문장 → 해당 가이드의 "그대로 쓰는 문장"이나 "실패→수정 표"에 근거(작품·job ID)와 함께.
- `guide/00`은 짧게 유지한다(4천 자 안팎). 길어지면 내용을 `01`로 옮긴다.
- 한 번만 확인된 것은 규칙이 아니라 "관찰"로 적는다. 서로 다른 사례 두 개가 모이면 규칙으로 올린다.
