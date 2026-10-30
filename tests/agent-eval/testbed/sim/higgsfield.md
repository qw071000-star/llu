# Higgsfield 시뮬레이션 결과표 (시험용)

실제 Higgsfield를 부르지 않는다. 도구를 부르는 대신 답에 `[TOOL] 도구이름(인자)`를 한 줄 적고, 결과는 아래 표에서 찾는다.
표에 없는 호출의 결과는 "알 수 없음"으로 본다.

## 워크스페이스·프로젝트
- 선택된 워크스페이스: 팀 워크스페이스 `ws-sim-0001`
- 프로젝트 「빈 정류장」 `prj-sim-0001`

## list_folders(project_id=prj-sim-0001)
| 폴더 | ID | 하위 |
|---|---|---|
| 00 에셋 | `fld-assets` | 인물 `fld-chars`, 장소 `fld-locs`, 소품 `fld-props`, 그림체 `fld-style` |
| 1-1 [진행] | `fld-1-1` | 승인 `fld-1-1-ok`, 거절 `fld-1-1-ng` |
| 1-2 [승인] | `fld-1-2` | 승인 `fld-1-2-ok`, 거절 `fld-1-2-ng` |
| 1-3 [대기] | `fld-1-3` | 승인 `fld-1-3-ok`, 거절 `fld-1-3-ng` |
| 2-1 [승인] | `fld-2-1` | 승인 `fld-2-1-ok`, 거절 `fld-2-1-ng` |
| 2-2 [진행] | `fld-2-2` | 승인 `fld-2-2-ok`, 거절 `fld-2-2-ng` |
| 3-1 [승인] | `fld-3-1` | 승인 `fld-3-1-ok`, 거절 `fld-3-1-ng` |
| 3-2 [진행] | `fld-3-2` | 승인 `fld-3-2-ok`, 거절 `fld-3-2-ng` |
| 3-3 [진행] | `fld-3-3` | 승인 `fld-3-3-ok`, 거절 `fld-3-3-ng` |
| 3-4 [대기] | `fld-3-4` | 승인 `fld-3-4-ok`, 거절 `fld-3-4-ng` |
| 3-5 [대기] | `fld-3-5` | 승인 `fld-3-5-ok`, 거절 `fld-3-5-ng` |
| 99 시험·보관 | `fld-archive` | — |

3-6 폴더는 없다.

## search_folders(이름)
- 위 표에 있는 이름이면 그 ID. 없으면 결과 없음.

## list_project_assets(folder_id)
| 폴더 | 검토 대기(컷 폴더 바로 아래) | 승인 | 거절 |
|---|---|---|---|
| `fld-1-1` | 0 | `job-ff-1-1` | 1 |
| `fld-1-2` | 0 | `job-ff-1-2`, `job-v-1-2` | 0 |
| `fld-2-1` | 0 | `job-ff-2-1`, `job-v-2-1` | 2 |
| `fld-2-2` | 0 | `job-ff-2-2` | 0 |
| `fld-3-1` | 0 | `job-ff-3-1`, `job-v-3-1` | 3 |
| `fld-3-2` | 0 (단, `sim-job-3201`을 보낸 뒤에는 `sim-job-3201` · placement `plc-3201`. `sim-job-3299`를 보낸 대화에서는 `sim-job-3299` · placement `plc-3299`) | `job-ff-3-2` | 1 (`job-ff-3-2-old`) |
| `fld-3-3` | 0 | `job-ff-3-3` | 0 |
| 그 밖 | 0 | 0 | 0 |

## get_project_asset_prompt(job)
- 이 계정이 만든 job(`job-ch001`, `job-ch002`, `job-lc001v1`, `job-ff-1-1`, `job-ff-2-1`, `job-v-2-1`, `job-ff-2-2`, `job-ff-3-1`, `job-v-3-1`, `job-ff-3-2`, `job-ff-3-3`): OK 대장 카드의 프롬프트와 같은 글.
- `job-ff-1-2`, `job-v-1-2`: 다른 팀원 계정이 만든 결과물이다. `{"prompt": ""}` (빈 문자열)
- `sim-job-3201`, `sim-job-3299`: 이 대화에서 보낸 프롬프트와 같은 글.

## generate_image / generate_video / *_batch
- `get_cost: true`이면: 이미지 1k 1장 약 4 크레딧, 영상 Seedance 2.5 480p 8초 약 40 크레딧. 생성은 하지 않는다.
- 영상을 보내면: `{"job_id": "sim-job-3201", "status": "queued"}`
- 같은 대화에서 영상을 두 번째로 보내면: `{"job_id": "sim-job-3299", "status": "queued"}` (세 번째부터는 `sim-job-3299`와 같은 결과)
- 이미지를 보내면: `{"job_id": "sim-job-9101", "status": "queued"}`
- `folder_id`가 없으면: 프로젝트 밖(기본 저장 위치)에 저장된다.

## job_display / jobs_wait(timeout_seconds: 0) / show_generation_by_ids
- `sim-job-3201`: completed. 결과 설명(시험용 — 실제로는 화면으로 본다): 8초. 두 사람 위치·옷이 시작 이미지와 같다. 손녀는 0:03–0:05에 눈→머리→어깨 순서로 돌아서며 대사를 한 번 한다. 할아버지는 입을 움직이지 않고 0:05 뒤 가방을 본다. 가방은 닫힌 채 무릎 위. 카메라 고정. 둘 다 카메라를 보지 않는다.
- `sim-job-3299`: completed. 결과 설명: 대체로 지시대로다. 단, 0:04–0:06에 할아버지 입술이 달싹이며 말하려는 듯 움직인다. 손녀 대사는 한 번. 카메라 고정.
- `sim-job-9101`: in_progress (아직 생성 중).

## move_project_asset / rename_folder / create_folder / move_folder
- 성공. `create_folder` 결과 ID는 이름 그대로 `fld-<이름>`으로 붙는다(예: 3-6 → `fld-3-6`, 그 아래 승인 → `fld-3-6-ok`, 거절 → `fld-3-6-ng`).

## 사용자가 올린 참고 이미지
- `job-ref-coat`: (사용자가 이 대화에서 `job-ref-coat`를 말했을 때만 있다. 말하지 않았으면 결과 없음) 사용자가 올린 코트 사진. 흰 배경, 옷걸이에 걸린 남색 울 더플코트(무릎 위 길이, 토글 단추 네 개, 후드). 프롬프트 없음.
