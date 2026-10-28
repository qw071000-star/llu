# 원본 자료 색인 — 이 지침이 어디서 왔나

가이드(`guide/`)는 아래 원본을 일반화해 합친 것이다. 원본은 지우거나 고치지 않았다. 규칙이 모호하면 원본을 확인한다.

## 1. 이 리포 루트의 원본 (「어머니와 고등어」 프로젝트 지침·컨텍스트, 2026-09-23~25)

| 원본 파일 | 내용 | 통합된 곳 |
|---|---|---|
| `확정 사항 — 「어머니와 고등어」.md` | 작품 확정 사항 §1~§8, 미결 17건. §8은 크레딧이 헛쓰인 원인 5가지 | `guide/00`·`01`·`07`, `templates/decisions.md` |
| `production-os-prompt-guide.md` | 15단계 프롬프트 규범(§1~§31) + 부록(광학·연기·실제 생성 패턴) | `guide/03`, `templates/video-prompt.md` |
| `the-prompter-씬1-분석..md` | 다른 작품(The Prompter) Seedance 2.5 영상 66개 분석 — 블록·요소·실패→수정 | `guide/03`·`05`·`07` |
| `acting-guide.md` | 연기 공리, 마스터 프로필 5인, 레지스터, 실패 아틀라스, 검증 문장 | `guide/05` |
| `character-sheet-guide..md` | 3패널 인물 시트, 수정 문법, 인물 명세 | `guide/04` §3, `templates/image-prompts.md` |
| `location-guide.md` | 장소 통제(모드 판별, 권한 5단계, 좌표, 시대, 마감 세트) | `guide/04` §0·§1·§4 |
| `location-templates.md` | 장소 작업별 템플릿 01~12(이 영화 규칙 반영본) | `guide/04` §2, `templates/image-prompts.md` |
| `location-assets.md` | 장소 에셋 대장(LC-002 뷰 계보, MASTER GEOMETRY 초안) | `templates/asset-registry.md` |
| ` 01. 레퍼런스 권한 분리.md` ~ `12. 다단계 제작과 버전 계보.md`, `00. 인덱스.md` | 옛 장소 가이드 시리즈(The Prompter 원문 기반, 축약 전 판). 파일명 앞 공백 주의(` 01.`) | `location-templates.md`가 이것의 정리본 |
| `힉스필드_장소_에셋_실제_프롬프트_모음.md` | The Prompter 장소 프롬프트 원문 20개 | 근거 자료 |
| `템플릿 검증 시나리오.md`, `추가 검증 원문.md` | 템플릿 대입 검증, 규칙 승격 기준(서로 다른 원문 2개) | 근거 자료 |
| `콘티 데이터 — 위치와 구조.md` | 콘티 사이트 JSON 구조, 컷 한 개가 네 곳에 나뉜 구조, 수정 순서 | `guide/02` §7 |
| `conti.lucianwork.com 작업 정리 & 수정 가이드.md` | 콘티 사이트(Cloudflare Worker·R2) 운영, 동기화 충돌 위험 | `guide/02` §7, `07` E-40 |

## 2. Claude Docs 문서 (나부코 '히브리 노예들의 합창' 배경 영상 작업, 2026-10-22~28)

| 문서 | 링크 | 통합된 곳 |
|---|---|---|
| AI 수채 풍경 배경 영상 제작 지침서 (작성 중 — 7개 절 미작성) | https://claude.ai/artifact/QDCfEME4DXGq68sWBPprWp | `guide/00`·`01`·`07`, `templates/decisions.md` §0 |
| 아침 컷 최종본 (GPT Image 2.5 + Kling 4.0) | https://claude.ai/artifact/2fkRLyhPXnzfPgCqsTTUXB | `guide/03` §3, `04` §6, `templates/` |
| N1~N5 아침 프롬프트 (최종) | https://claude.ai/artifact/TaETSZ8qeDiYtKwf62Beow | `guide/04`, `07` E-28·E-29 |
| N1~N5 최종 프롬프트와 검증 | https://claude.ai/artifact/GCFcoY4r1jMbPdHjaWxPTW | `guide/04`, `07` E-27 |
| N1~N5 확장 샷 계획과 프롬프트 | https://claude.ai/artifact/LfMw7AJFh7CmZM58aqZy11 | `guide/04` §7 |
| 전주 3 회상 장면 자료 모음 | https://claude.ai/artifact/EqWxNqgeDEvM1FwrdvGJjJ | `guide/04` §4(시대), `07` E-37·E-41 |
| 1구간 수정안 (구성 수정안 — 1구간 풀샷부터 사해까지, 266회 개정) | https://claude.ai/artifact/97Um62UNWgQ17cawiCKBUD | `guide/03`·`04`·`06`·`07` 대부분의 나부코 사례 |
| 2구간 ③ ~ 후주 구성안 | https://claude.ai/artifact/MnxAnQbhFxwuJor6wXy2dL | 근거 자료 |

## 3. Higgsfield (워크스페이스 1개)

| 프로젝트 | ID | 내용 |
|---|---|---|
| 고등어 | `721fc8ec-6205-4be9-a3e7-b9873b14ff18` | 「어머니와 고등어」 씬 1 실사. 폴더 #1·인물·장소·소품 |
| 어머니와 고등어 — 씬 1 | `c5307199-b7a2-40ae-b37a-9ff46b6b635a` | 비어 있음 |
| 히브리 | `df31e9d3-4a62-458e-b266-97bf9bc16e93` | 나부코 배경 영상. 폴더 전주1·1·2·3·4·N |
| 새 프로젝트 | `251de165-a03d-487c-b40e-6a7bbbd0306c` | 10/19–20 초기 시험 |
| New folder | `06fb52fe-83f6-4533-a75f-efbd9283f684` | 비어 있음 |

분석: `analysis/higgsfield-history.md`.

## 4. 다른 작업에서 가져온 운영 교훈

| 출처 | 가져온 것 | 통합된 곳 |
|---|---|---|
| 리포 `personal` (`AGENTS.md`, `docs/CHAT_COORDINATION_PROMPTS.md`) | 메인 채팅 + 서브 채팅 체계: 받는 채팅 라벨, HANDOFF 형식, `resolved_by_subchat` vs `closed`(메인만 닫음), 파일 소유·충돌 규칙. 반대로 로그 문서가 80만 자를 넘어 읽기 비용이 커진 점 | `guide/02`, `templates/cut-card.md`·`handoff.md`, `07` E-39 |
| 다른 Claude 세션(Topaz 문의) | Claude Code 세션은 Claude 앱 프로젝트 대화를 읽지 못한다 → 파일로 공유 | `guide/02` §7, `07` E-41 |
| 다른 Claude 세션(자막 OCR 프로토타입) | 정답 데이터로 비교하는 검증 습관 | `guide/06` §2의 취지 |
| 리포 `lulu`(FCP 자막 앱), `freepick-mac`(가격 모니터 앱) | 영상 제작 지침과 무관한 코드 프로젝트 — 사용하지 않음 | — |

## 5. 확인하지 못한 것

- 리포 `lucianwork-conti`(콘티 사이트 백업 저장소): 이번 세션에서 연결 요청이 권한 정책으로 거부되어 열어 보지 못했다. 콘티 JSON(`embeddedAssetData.json` 등)과 사이트 쪽 `CLAUDE.md`가 있을 것으로 보인다.
- Claude 앱 프로젝트 「고등어」의 대화 원문: Claude Code 세션에서는 읽을 수 없다. 이 리포에 올린 문서가 그 대신이다.
- Higgsfield 영상·이미지 자체(직접 열어 보지 않음).
