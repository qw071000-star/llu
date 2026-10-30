# conti.lucianwork.com 작업 정리 & 수정 가이드
 
작성: 2026-09-24 · 보완: 2026-09-24 (스크립트·Worker 코드 대조 후 위험 구간과 개선 과제 추가)
 
---
 
## 0. 먼저 기억할 세 줄
 
1. **사이트(R2)가 원본이다.** 맥 폴더는 백업 사본이다. 맥 파일만 고치면 사이트에 안 보인다.
2. 파일을 직접 고칠 때는 **사이트 탭을 모두 닫고** → `pull` → 수정 → `push` → 탭을 새로 연다.
3. **동기화에는 충돌 감지가 없다.** 같은 파일을 두 곳에서 고치면 나중에 저장한 쪽이 조용히 이긴다(§3-④).
---
 
## 1. 지금 구조 한눈에 보기
 
```
[브라우저] ──▶ Cloudflare Access (Cloudflare 계정 로그인)
                 │
                 ▼
          Cloudflare Worker `conti-lucianwork`  ──▶  R2 버킷 conti-data   ← 사이트의 "원본"
           · conti.lucianwork.com                    │
           · conti-beta.lucianwork.com  (같은 R2!)    │  맥이 켜져 있을 때 1분마다 R2 → 맥 (바뀐 것만)
           · *.workers.dev  (관리 API 전용)           ▼
                                   맥 폴더 ~/Documents/LucianWork_Page   ← 백업 사본
                                                     │  1분마다 git commit·push
                                                     ▼
                                   GitHub 비공개 저장소 lucianwork-conti  ← 변경 이력
```
 
- **맥을 꺼도 사이트는 동작**한다. 단, 맥이 꺼져 있는 동안의 저장은 **이력이 남지 않는다**(§5).
- **나만 볼 수 있음**: Cloudflare Access 앱 `conti`, 정책 `나만` (qw07100@naver.com). Worker도 Access 토큰(JWT)을 직접 한 번 더 검증한다.
- **`conti-beta`는 테스트 데이터가 아니다.** 같은 Worker·같은 R2를 쓴다. beta에서 고치면 실제 콘티가 바뀐다.
- 비용: 무료 한도 안(R2 10GB 무료, 현재 약 0.03GB).
---
 
## 2. 오늘 한 작업
 
| 단계 | 내용 | 결과 |
|---|---|---|
| ① GitHub 백업 | 비공개 저장소 `lucianwork-conti`, 1분마다 자동 커밋·push | 소스·데이터 유실 위험 해소 |
| ② 구조 분리 | 컷 사진 39장(20MB JSON 1개) → 컷별 이미지 파일 + 화면용 축소본(WebP) | 첫 화면 전송량 **21MB → 약 0.3MB** |
| ③ Cloudflare 이전 | Express 서버 → Cloudflare Worker, 데이터 → R2 | 맥 없이 24시간 동작 |
| ④ 접근 제한 | Cloudflare Access + Worker 자체 JWT 검증(이중 잠금) | 나만 접속 가능 |
| ⑤ 자동 백업 | R2 → 맥 → GitHub, 1분 주기 (`ops/auto-sync.mjs`, launchd) | 맥이 켜져 있는 동안 이력 보관 |
| ⑥ 맥 서버 정리 | 예전 Express 서버·Cloudflare Tunnel 종료 | 되돌리기 스크립트로 재가동 가능 |
 
### 달라진 사용 감각
 
- 컷 사진 교체: 예전처럼 **더블클릭 / 2초 길게 누르기**. 원본 + 축소본이 함께 저장된다.
- **우클릭 → 이미지 저장** 하면 원본이 저장된다(화면엔 축소본).
- **"HTML로 저장"**: 예전과 같이 모든 이미지를 품은 단일 HTML 파일로 저장된다.
---
 
## 3. 콘티를 수정하는 방법
 
### ① 사이트에서 편집 (평소 작업)
 
`https://conti.lucianwork.com` 에서 편집 → 자동저장 → R2. 맥이 꺼져 있어도 된다.
**탭은 하나만 연다.** 캐릭터·의상·컷 텍스트는 파일째 저장되므로, 두 탭(또는 두 기기)에서 같은 문서를 열어 두면 늦게 저장한 탭이 먼저 저장한 내용을 덮는다.
 
### ② 파일을 직접 고칠 때 (다른 Claude 세션 / 직접 수정)
 
```bash
cd ~/Documents/LucianWork_Page
 
# 0. 사이트 탭을 모두 닫는다 (열린 탭이 나중에 자동저장하면 내 수정이 사라진다)
node worker/scripts/pull-r2.mjs     # 1. 사이트의 최신 내용 받기
cp <고칠 파일> pages/archive/<파일명>.<YYYYMMDD-HHMMSS>.bak   # 2. 백업
#                                     3. 수정 (JSON은 저장 후 python3 -m json.tool 로 검사)
node worker/scripts/push-r2.mjs     # 4. 사이트에 반영 (바뀐 파일만)
#                                     5. 사이트를 새로 열어 확인
```
 
- 1 → 4 사이는 **짧게**. 이 사이에 사이트에서 같은 파일이 바뀌면 둘 중 하나가 사라진다(아래 ④).
- 한 파일만 올리려면: `node worker/scripts/push-r2.mjs pages/<문서>.data/embeddedAssetData.json`
- 이 규칙은 프로젝트 폴더의 **`CLAUDE.md`** 에도 있어 다른 Claude 세션이 따른다.
**어떤 파일을 고치나?**
 
| 바꾸고 싶은 것 | 파일 |
|---|---|
| 화면·기능(앱 코드), 컷 원본 텍스트(`var SC`) | `pages/어머니와_고등어_Main_V3.1.html` |
| 컷 텍스트 덮어쓰기(desc·note·camera) | `…data/embeddedTextOverrides.json` |
| 캐릭터·의상·캐스팅 | `…data/embeddedCharacterData.json` |
| 에셋·씬·컷·뷰 배정 | `…data/embeddedAssetData.json` |
| 컷 사진 목록 | `…data/embeddedFrameImages.json` (`{컷: {src, thumb}}` 주소만) |
| 컷 사진 파일 | `frames/어머니와_고등어_Main_V3.1/<컷>-<시각>.jpg|png` + `.thumb.webp` |
| 업로드 이미지·영상, 인물 사진 | `uploads/<문서>/` |
| 새 프로젝트 페이지 | `pages/<새이름>.html` 추가 후 push |
 
### ③ 동기화되지 않는 것 — 알고 쓰기
 
| 무엇 | 동작 |
|---|---|
| `pages/archive/`, `pages/.claude_backups/`, 이름이 `.`으로 시작하는 파일 | R2에 올라가지 않는다. archive는 GitHub에는 남고, `.claude_backups/`는 GitHub에도 없다(.gitignore) → **백업은 `pages/archive/`에** |
| 파일 **삭제·이름 변경** | pull도 push도 지우지 않는다. 맥에서 지운 파일은 R2에 남고, 이름을 바꾸면 R2에 옛 이름이 남는다 |
| 허용된 경로 밖의 파일 | pull·push 대상은 `pages/*.html`, `pages/*.data/*.json`, `frames/`, `uploads/`뿐이다 |
| JSON 속 `<` | R2에는 `<`로 저장된다(유효한 JSON 그대로). pull 받은 파일에서 `<`로 검색하면 안 걸린다 |
 
### ④ 동시에 고치면 무슨 일이 나나 (충돌 감지 없음)
 
| 상황 | 결과 |
|---|---|
| pull 뒤, push 전에 **사이트에서 같은 파일을 저장** | push가 사이트의 저장을 **덮어쓴다** |
| 맥에서 고치는 중(push 전)에 **사이트에서 같은 파일을 저장** | 1분 안에 자동 동기화가 R2 판을 내려받아 **맥의 수정을 덮어쓴다** |
| push 뒤, **열려 있던 옛 탭이 자동저장** | 캐릭터·의상·컷 텍스트는 탭이 `embeddedCharacterData`·`embeddedTextOverrides`를 **파일째** 저장하므로 push한 내용을 **덮어쓴다**. 에셋 목록·프롬프트는 서버가 항목 단위로 합쳐 저장해 덜 위험하다 |
| 서로 **다른 파일**을 고침 | 문제없다 |
 
덮어써진 쪽은 GitHub 이력에서 되찾을 수 있다 — **맥이 켜져 있어 1분 주기 커밋이 돌았을 때만.**
 
### ⑤ 사이트 기능(서버 코드)을 바꿀 때
 
`worker/src/index.js` 수정 → 테스트(`worker/README.md`) → 배포:
 
```bash
cd ~/Documents/LucianWork_Page/worker && npx -y wrangler@4 deploy
```
 
- 무료 플랜 한도: 요청당 CPU 10ms. 큰 JSON을 통째로 문자열 변환·재직렬화하지 않는다(`worker/README.md`).
- 예전 `src/server.ts`(Express)는 사이트에 쓰이지 않는다(되돌리기용).
---
 
## 4. 자주 쓰는 명령 모음
 
```bash
cd ~/Documents/LucianWork_Page
 
node worker/scripts/pull-r2.mjs              # R2 → 맥 (최신 받기)
node worker/scripts/push-r2.mjs              # 맥 → R2 (바뀐 것만)
node worker/scripts/push-r2.mjs <파일경로>    # 맥 → R2 (그 파일만)
node worker/scripts/push-r2.mjs --all        # 맥 → R2 (전부 다시 — 사이트의 최신 저장을 덮을 수 있음)
cd worker && npx -y wrangler@4 deploy        # Worker 코드 배포
 
zsh worker/scripts/mac-server.sh status      # 맥 서버·터널·자동백업 상태
zsh worker/scripts/mac-server.sh stop        # 맥 서버·터널 끄기
zsh worker/scripts/mac-server.sh start       # 맥 서버·터널 켜기
 
zsh worker/scripts/cutover.sh --rollback     # 비상시: 사이트를 다시 맥 서버로
tail -20 ops/gitsync.log                     # 자동 백업이 도는지 확인
```
 
---
 
## 5. 문제가 생겼을 때
 
| 증상 | 대처 |
|---|---|
| 사이트가 이상하게 동작 | `cutover.sh --rollback` → 맥 서버가 다시 켜지고 사이트가 맥으로 돌아감 |
| 파일을 고쳤는데 사이트에 안 보임 | `push-r2.mjs` 실행했는지 → 사이트 탭을 **새로** 열었는지 |
| push한 내용이 잠시 뒤 옛 내용으로 돌아감 | 열려 있던 옛 탭이 자동저장한 것. 탭을 닫고 다시 push |
| 맥에서 고친 내용이 사라짐 | 그 사이 사이트에서 같은 파일이 저장돼 자동 동기화가 덮은 것. GitHub 이력에서 내 판을 찾아 복원 → push |
| 예전 버전으로 되돌리고 싶음 | GitHub `lucianwork-conti` 커밋 이력에서 파일 복원 → push |
| 로그인 화면이 계속 뜸 | Cloudflare 계정(qw07100@naver.com)으로 로그인 |
| 맥 백업이 멈춘 것 같음 | `ops/gitsync.log` 확인 (1분마다 기록). `R2 내려받기 실패`가 이어지면 네트워크·토큰 확인 |
| 관리 토큰이 새었을 수 있음 | `cd worker && npx -y wrangler@4 secret put ADMIN_TOKEN`으로 새 값 설정 → `ops/r2-sync.json`의 `token`을 같은 값으로 교체 |
 
**이력의 빈틈**: R2는 덮어쓸 때 옛 판을 남기지 않는다. 맥이 꺼져 있는 동안 같은 문서를 여러 번 저장하면, 맥이 켜졌을 때 마지막 판 하나만 GitHub에 남는다.
 
---
 
## 6. 개선 과제 (아직 안 한 것)
 
위험이 큰 순서다. 스크립트·Worker 코드를 고치는 일이라 적용 전 테스트가 필요하다.
 
| # | 과제 | 막는 사고 | 방법 |
|---|---|---|---|
| 1 | **push 충돌 검사** | pull 이후 사이트에서 저장된 내용을 push가 덮음 | push 전에 `list`로 R2의 현재 etag를 받아, 마지막 pull 때의 etag(`ops/.r2-pull-manifest.json`)와 다르면 그 파일은 올리지 않고 경고. `--force`일 때만 덮기. push가 받은 새 etag를 pull 매니페스트에도 기록 |
| 2 | **pull 충돌 검사** | 맥의 미반영 수정을 자동 동기화가 덮음 | 내려받기 전에 로컬 파일이 마지막 동기화 이후 바뀌었으면(push 매니페스트 서명과 다르면) 덮지 않고 `<파일>.r2-conflict`로 R2 판을 따로 저장 |
| 3 | **Worker 저장 이력** | 맥이 꺼져 있는 동안의 저장 이력 공백 | 데이터 JSON을 저장할 때 직전 판을 `history/<key>/<시각>`으로 복사하고 N개만 보관. 또는 Worker Cron으로 하루 한 번 스냅샷 |
| 4 | **옛 탭 저장 거부** | push 뒤·다른 탭에서 옛 탭이 자동저장해 덮음 | 캐릭터 저장(`apiCharacters`)은 이미 서버에서 `revision`을 읽어 +1 한다. 탭이 들고 있던 revision을 함께 보내게 하고, 서버 값과 다르면 409로 거부 + "새로고침 필요" 안내. push 스크립트도 revision을 올리게 맞춘다 |
| 5 | **삭제 반영 옵션** | 맥에서 지운 파일이 R2에 남음 | `push-r2.mjs --prune`(확인 후 R2에서 삭제) |
| 6 | `conti-beta` 정리 | 테스트인 줄 알고 실제 데이터를 고침 | 검증이 끝났으면 route에서 빼거나, 별도 버킷으로 분리 |
 
1·2는 맥 스크립트만 고치면 된다. 3·4는 Worker 배포가 필요하다.
 
---
 
## 7. 관련 위치
 
- 사이트: https://conti.lucianwork.com (beta: https://conti-beta.lucianwork.com — **같은 데이터**)
- Cloudflare 대시보드: Workers `conti-lucianwork`, R2 `conti-data`, Access 앱 `conti`
- GitHub: `lucianwork-conti` (비공개)
- 설계 문서: `docs/CLOUDFLARE_MIGRATION_PLAN.md`, `worker/README.md`, `CLAUDE.md`
- 동기화 설정: `ops/r2-sync.json` (관리 API 주소·토큰, GitHub에 올라가지 않음)