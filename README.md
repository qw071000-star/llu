# llu — AI 이미지·영상 제작 지침 키트

「어머니와 고등어」(실사 단편), 나부코 '히브리 노예들의 합창'(수채 배경 영상), The Prompter 분석, Higgsfield 생성 기록 930건에서 확인된 규칙과 실수를 모았다. **어느 프로젝트에나 넣어 쓸 수 있게** 정리한 키트다.

목표는 네 가지다.
1. 새 대화마다 같은 설명을 반복하지 않는다.
2. 다른 작업에서 했던 실수를 다시 하지 않는다.
3. 크레딧과 토큰을 헛쓰지 않는다.
4. 결과물이 정해진 폴더에 상태(승인·거절)와 함께 정리된다.

---

> 팀원에게 처음 공유할 때는 [`TEAM-GUIDE.md`](TEAM-GUIDE.md)를 함께 보내세요. Higgsfield와 MCP를 처음 쓰는 사람을 위한 안내서입니다.

## 구조 — 무엇이 언제 읽히나

```
kit/                                  ← 다른 프로젝트에 넣는 것
  instructions.md                     ← [항상] 지침 칸 / CLAUDE.md. 약 3,500자
  skills/                             ← [그 작업을 할 때만] 스킬 안에서도 단계 파일 하나만 읽는다
    project-setup/                    새 작품 시작: 질문 한 번, 정본 초안, Higgsfield 폴더
    production-session/               세션 시작·컷 카드·핸드오프·정본 관리
    higgsfield-generation/            저장 폴더·요청 후 턴 끝내기·승인/거절 표시·검수·크레딧
                                      + check_prompt.py (생성 전 프롬프트 자동 검사)
    image-prompt/                     공통 규칙 + character / location / prop / style / first-frame
    video-prompt/                     공통 규칙 + live-action / background / fixes / rerender
    acting/                           인물 연기
  project-files/                      ← [작품마다 복사해 채움] 정본 세 개 + Claude Code용 CLAUDE.md
  dist/*.zip                          ← Claude 앱에 올리는 스킬 묶음 (pack-skills.sh로 다시 만든다)
reference/                            ← [컨텍스트에 넣지 않음] 사람이 근거를 볼 때만
  error-registry.md                   오류 대장 E-01~E-47
  higgsfield-history.md               Higgsfield 전 프로젝트 분석: 잘된 것·안 된 것·크레딧
  context-research.md                 Claude 컨텍스트 운영 사용자 사례 43건과 반영 내역
  source-index.md                     원본 자료 색인
  public-projects-study.md            Higgsfield 공개 프로젝트 3개(Cully Hill Boys·BESA·The Kiss) 연구
archive/어머니와-고등어/                ← [컨텍스트에 넣지 않음] 원본 24개. 그 작품을 이어갈 때만
```

**한 번에 읽히는 양 (글자 수)**

| 상황 | 예전(가이드 전부를 지식에) | 지금 |
|---|---:|---:|
| 모든 대화의 기본 | 약 64,600 | 약 5,000 (지침 + 스킬 설명 6개) + 정본 |
| 퍼스트 프레임 만들기 | 약 64,600 | + 약 9,400 (이미지 공통 + first-frame + 생성 운영) |
| 실사 컷 영상 프롬프트 새로 쓰기 | 약 64,600 | + 약 17,100 (영상 공통 + live-action + acting + 생성 운영) |
| 영상 프롬프트 고치기 | 약 64,600 | + 약 5,000 (영상 공통 + fixes) + 그 job의 확정 프롬프트 |

---

## 설치 — Claude 앱 (Projects)

**1. 스킬 올리기 (계정에 한 번)**
- 설정에서 코드 실행을 켠다. 스킬은 코드 실행이 켜져 있어야 동작한다.
- 스킬 메뉴(Customize → Skills 또는 Settings → Capabilities)에서 `kit/dist/`의 zip 여섯 개를 하나씩 올린다.
- 스킬은 계정 단위라 모든 프로젝트에서 같이 쓴다. 작품마다 다시 올리지 않는다.

**2. 작품마다 프로젝트 만들기**
- 커넥터에서 Higgsfield와 Claude Docs를 켠다.
- 지침 칸에 `kit/instructions.md`를 붙인다. "이 프로젝트" 칸은 비워 둔다.
- 첫 대화에서 하고 싶은 일을 말하면 Claude가 다음을 진행한다.
  1. 시작 질문을 한 번에 한다.
  2. 정본을 Claude Doc 하나로 만든다.
  3. Higgsfield 폴더 구성을 제안한다.
  4. "이 프로젝트" 세 줄(작품명, Higgsfield 프로젝트 ID, 정본 Doc 링크)을 알려 준다. 그걸 지침 칸에 붙이면 끝이다.
- 프로젝트 지식에는 아무것도 올리지 않아도 된다. Docs를 쓰지 않는다면 정본 세 개만 올린다.
  - 가이드나 `reference/`, `archive/`는 올리지 않는다. 지식은 모든 대화가 전부 읽는다.

**3. 스킬을 쓸 수 없는 환경이면**
- `kit/skills/`의 파일을 프로젝트 지식에 올린다.
- 모든 대화가 전부 읽어서 무거워지지만, 따로 첨부하지 않아도 자동으로 읽힌다.

## 설치 — Claude Code (작품 리포)

```bash
mkdir -p .claude project/cuts project/log
cp kit/instructions.md .claude/instructions.md
cp -r kit/skills .claude/skills
cp kit/project-files/CLAUDE.md CLAUDE.md
cp kit/project-files/{decisions,asset-registry,shot-list}.md project/
```

선택 사항: 작업이 끝날 때 휴대폰 알림을 받고 싶으면 Claude Code의 Stop 훅으로 알림을 보낸다(ntfy 등, `reference/context-research.md` E절).

---

## 새 대화

시작 문구는 필요 없다. 새 대화에서 바로 일을 말하면 된다(예: "C03 퍼스트 프레임", "인물 시트 고치자").
Claude는 답하기 전에 다음을 스스로 한다.
1. 정본을 읽는다.
2. 첫 메시지로 총괄인지 컷 작업인지 판단한다.
3. Higgsfield 폴더 상태, 마지막 핸드오프, 필요한 스킬 파일을 직접 가져온다.
4. 그래도 모르는 것만 기본값과 함께 한 번에 묻는다.

정본이 비어 있으면 새 작품으로 보고, 시작 질문부터 한다(`project-setup`).

---

## Higgsfield 폴더

처음 작업할 때 Claude가 아래 구성을 제안하고 "제가 만들까요, 직접 만드시겠어요?"라고 묻는다.

```
「작품명」
├─ 00 에셋 / 인물 · 장소 · 소품 · 그림체
├─ C01 [진행]  ─ 승인 · 거절        ← 새 결과는 컷 폴더에, 판정 후 승인·거절로 이동
├─ C02 [대기]
└─ 99 시험·보관                      ← 시험 생성, 교체된 옛 승인본
```

- 폴더 ID는 `asset-registry.md`의 폴더 표에 적힌다.
- 결과를 보고 "좋아"라고 하면 승인 폴더로, "별로"라고 하면 거절 폴더로 옮겨진다.
- 컷 상태는 폴더 이름(`C01 [승인]`)과 `shot-list.md`에 같이 표시된다.

---

## 키트를 고칠 때

- **새 실수:** `reference/error-registry.md` 맨 아래에 E-48부터 추가한다. 그 규칙을 `kit/`의 해당 파일에 한 줄로 넣는다.
  - 모든 대화에서 지켜야 하면 `instructions.md`에, 특정 작업에서만이면 그 스킬에 넣는다.
- **`instructions.md`는 4천 자를 넘기지 않는다.** 길어지면 스킬로 옮긴다.
- **한 번만 확인된 것은 "관찰"로 적는다.** 서로 다른 사례 두 개가 모이면 규칙으로 올린다.
- **kit 안에는 규칙과 빈 틀만 둔다.** 사례, 작품 이름, 통계는 `reference/`에 둔다. 이전 작품의 고유 명사는 새 작품 프롬프트로 샌다.
- **스킬을 고치면** `kit/pack-skills.sh`를 실행해 zip을 다시 만들고 Claude 앱에 다시 올린다.
