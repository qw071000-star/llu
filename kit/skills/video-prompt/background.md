# 배경·풍경·그림체 영상 — 4문단

인물 연기가 없고, 시작 이미지가 장면을 다 담고 있을 때 쓴다.

## 규칙

- **정보 점검은 `SKILL.md` §0의 배경 표로 한다.** 설정 · `Camera` · `Motion` · `Keep`(유지할 형태·빛 방향) · `Silent` 칸을 다 채운다. `Keep`은 사용자가 말하지 않아도 제안값으로 보인다.
- **네 문단(`Camera` / `Motion` / `Keep` / `Silent`)으로 쓴다.**
- **이미지에 이미 있는 것을 다시 묘사하지 않는다.** 일어나는 움직임만 쓴다.
- **끝 상태, 페이드인, 다음 컷과의 이음새는 쓰지 않는다.**
- **움직임의 양은 화면 비율(%)로 쓴다.** 미터나 초 단위 위치는 지켜지지 않는다.
- **서두르는 것처럼 보이면 사건을 하나 뺀다.**
- **카메라·길이·소리는 정본 값을 묻지 않고 "기본값으로 씀: …"에 적는다.** 적은 항목은 질문 목록에 다시 넣지 않는다. 카메라 움직임과 움직이는 대상은 합쳐 3개까지, 넘으면 하나를 빼자고 제안한다.
- **속도·움직임 추가·별 같은 말은 `SKILL.md` §0 "모호한 말" 표로 바꾼다.**
- **시작 이미지의 매체가 요청 매체와 다르면**(실사 이미지로 수채화 영상) 영상만 바꿀 수 없다. 시작 이미지부터 새로 만들자고 제안하고, 예외 범위(이 컷만 / 작품 전체)를 묻는다.
- **소리:** `decisions.md` 소리 줄대로 쓰고 묻지 않는다(대사 없는 컷 = 효과음만, 끝 문단 `Sound:`). 사용자가 무음이라 하면 옵션에서 끄고, 끌 수 없으면 `Silent` 문단을 쓴다.

## 틀

```text
Camera: a slow, steady [glide direction], moving about [N] percent of the frame [closer / width /
height] over the whole clip. The horizon stays level; no rotation, no tilt, no zoom.

Motion: [only things already in the image that move, each with direction and pace].

Keep the [medium] look, every [shape list], and the light from screen [left/right], the [object] side, exactly as in the
image; only the things named above move, slowly and without morphing or melting.

Silent: no dialogue, no music, no sound effects.
```

고정 카메라일 때 첫 문단: `Camera: completely locked off for the whole clip; no pan, no tilt, no zoom, no push-in.`
효과음일 때 끝 문단: `Sound: only [ambient sounds]; no dialogue, no music.`
