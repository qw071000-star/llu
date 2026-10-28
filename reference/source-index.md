# 원본 자료 색인 — 이 키트가 어디서 왔나

> 컨텍스트에 넣지 않는다. 규칙이 모호하거나 근거를 확인할 때 사람이 본다.

`kit/`은 아래 원본을 일반화해 합친 것이다. 원본은 내용을 고치지 않고 `archive/어머니와-고등어/`로 옮겼다.

## 1. 「어머니와 고등어」 원본 (`archive/어머니와-고등어/`, 2026-09-23~25)

| 원본 파일 | 내용 | 통합된 곳 |
|---|---|---|
| `확정 사항 — 「어머니와 고등어」.md` | 작품 확정 사항 §1~§8, 미결 17건. §8은 크레딧이 헛쓰인 원인 다섯 가지 | `kit/instructions.md`, `kit/project-files/decisions.md`, `reference/error-registry.md` |
| `production-os-prompt-guide.md` | 15단계 프롬프트 규범과 부록 | `video-prompt/live-action.md` |
| `the-prompter-씬1-분석..md` | 다른 작품(The Prompter)의 Seedance 2.5 영상 66개 분석 | `video-prompt/`, `acting/` |
| `acting-guide.md` | 연기 공리, 마스터 프로필 5인, 레지스터, 실패 아틀라스 | `acting/SKILL.md` |
| `character-sheet-guide..md` | 3패널 인물 시트, 수정 문법 | `image-prompt/character.md` |
| `location-guide.md` | 장소 통제(모드 판별, 권한 5단계, 좌표, 시대) | `image-prompt/SKILL.md`, `location.md` |
| `location-templates.md` | 장소 작업별 템플릿 01~12 | `image-prompt/location.md`, `location-view.md`, `location-edit.md` |
| `location-assets.md` | 장소 에셋 대장(LC-002 뷰 계보) | `kit/project-files/asset-registry.md` |
| `힉스필드_장소_에셋_실제_프롬프트_모음.md` | The Prompter 장소 프롬프트 원문 20개 | 근거 자료 |
| `콘티 데이터 — 위치와 구조.md`, `conti.lucianwork.com 작업 정리 & 수정 가이드.md` | 콘티 사이트 JSON 구조와 운영, 동기화 충돌 위험 | `production-session/SKILL.md` §6, `error-registry.md` E-40 |

## 2. Claude Docs 문서 (나부코 '히브리 노예들의 합창' 배경 영상, 2026-10-22~28)

| 문서 | 링크 | 통합된 곳 |
|---|---|---|
| AI 수채 풍경 배경 영상 제작 지침서 (작성 중, 7개 절 미작성) | https://claude.ai/artifact/QDCfEME4DXGq68sWBPprWp | `kit/instructions.md`, `decisions.md` §0 |
| 아침 컷 최종본 (GPT Image 2.5 + Kling 4.0) | https://claude.ai/artifact/2fkRLyhPXnzfPgCqsTTUXB | `video-prompt/background.md`, `image-prompt/style.md` |
| N1~N5 아침 프롬프트 (최종) | https://claude.ai/artifact/TaETSZ8qeDiYtKwf62Beow | `image-prompt/` |
| N1~N5 최종 프롬프트와 검증 | https://claude.ai/artifact/GCFcoY4r1jMbPdHjaWxPTW | `image-prompt/`, `higgsfield-generation/qa-metrics.md` |
| N1~N5 확장 샷 계획과 프롬프트 | https://claude.ai/artifact/LfMw7AJFh7CmZM58aqZy11 | `image-prompt/SKILL.md` §4 |
| 전주 3 회상 장면 자료 모음 | https://claude.ai/artifact/EqWxNqgeDEvM1FwrdvGJjJ | `image-prompt/location.md`(시대) |
| 1구간 수정안 (266회 개정) | https://claude.ai/artifact/97Um62UNWgQ17cawiCKBUD | 나부코 사례 대부분 |
| 2구간 ③ ~ 후주 구성안 | https://claude.ai/artifact/MnxAnQbhFxwuJor6wXy2dL | 근거 자료 |

## 3. Higgsfield (워크스페이스 1개)

| 프로젝트 | ID | 내용 |
|---|---|---|
| 고등어 | `721fc8ec-6205-4be9-a3e7-b9873b14ff18` | 「어머니와 고등어」 씬 1 실사. 폴더 #1·인물·장소·소품 |
| 어머니와 고등어 — 씬 1 | `c5307199-b7a2-40ae-b37a-9ff46b6b635a` | 비어 있음 |
| 히브리 | `df31e9d3-4a62-458e-b266-97bf9bc16e93` | 나부코 배경 영상. 폴더 전주1·1·2·3·4·N |
| 새 프로젝트 | `251de165-a03d-487c-b40e-6a7bbbd0306c` | 10/19–20 초기 시험 |
| New folder | `06fb52fe-83f6-4533-a75f-efbd9283f684` | 비어 있음 |

분석은 `reference/higgsfield-history.md`에 있다.

## 4. 다른 작업에서 가져온 운영 교훈

| 출처 | 가져온 것 | 통합된 곳 |
|---|---|---|
| 리포 `personal`(`AGENTS.md`, 채팅 조율 문서) | 가져온 것: 메인 채팅 + 서브 채팅 체계, 받는 채팅 라벨, HANDOFF 형식, 메인만 닫는 규칙. 반면교사: 로그 문서가 80만 자를 넘어 읽기 비용이 커진 점 | `production-session/` |
| 다른 Claude 세션(Topaz 문의) | Claude Code 세션은 Claude 앱 대화를 읽지 못한다. 그래서 파일로 공유한다 | `production-session/SKILL.md` §6 |
| 웹 사용자 사례 30여 건 | 짧은 상시 지침, 필요할 때만 읽는 스킬, 실수마다 한 줄, 상태는 파일에, 기다리지 않기 | 키트 구조 전체(조사 문서는 2026-10-28 삭제) |

## 5. 확인하지 못한 것

- **리포 `lucianwork-conti`(콘티 사이트 백업):** 세션 권한 정책이 연결을 거부해서 열어 보지 못했다.
- **Claude 앱 「고등어」 프로젝트의 대화 원문:** Claude Code 세션에서는 읽을 수 없다.
- **Higgsfield 영상·이미지 자체:** 직접 열어 보지 않았다. 프롬프트와 생성 기록만 분석했다.
