---
name: acting
description: AI 영상에서 인물 연기를 쓸 때 쓴다. 15블록의 CHARACTER_ACTING을 채울 때, 인물 마스터 프로필이나 목소리 문장을 만들 때, 연기가 과하거나 죽었을 때 쓴다. 증상은 감정 과잉, 무표정, 휙 도는 동작, 말하지 않을 인물의 입 움직임, 죽은 눈, 배경 인물이 얼어붙음 같은 것이다. 다루는 것: 목표와 행동, 손의 일, 눈의 삶, 상태 쓰기, 레지스터, 검증된 문장.
---

# 인물 연기

## 1. 원칙

**연기는 감정의 전시가 아니라 압력 아래의 행동이다.** 감정은 쓰지 않는다. 목표와 행동을 쓴다.

| 쓰지 않는다 | 쓴다 |
|---|---|
| 감정 형용사 | 상대를 향한 동사 |
| 대사 차례를 기다리는 빈 얼굴 | 상대 말이 끝나기 전에 시작되는 반응 |
| 대사를 따라 하는 몸짓 | 진짜 일을 하는 손 |
| 연기하는 얼굴(눈썹, 찡그림) | 생각하는 얼굴. 눈에 먼저 읽힌다 |

## 2. 장면마다 정할 것

1. **목표:** 이 상대에게서 지금 원하는 것(동사).
2. **장애와 대가:** 무엇이 막는가, 실패하면 무엇을 잃는가.
3. **전술:** 실패하면 바꾼다.
4. **비트:** 한 장면에 2~4번 바뀐다. 바뀔 때 행동(사이, 자세, 속도, 시선)으로 보인다.

## 3. 몸

- **손에 할 일을 준다.** 말하는 동안 손이 진짜 일을 한다.
- **하던 일을 멈추는 순간이 가장 강한 강세다.** 멈출 때 `does not startle; simply stops`를 붙인다.
- **거리 변화 = 비트 변화.** 0.5m 친밀, 1.2m 신뢰, 3.5m 경계.
- **지위는 몸에 있다.** 높으면 움직이지 않는 머리, 느린 동작, 답하기 전의 사이. 낮으면 부산함, 자기 접촉, 끊기는 말.
- **걸음에 이름을 붙인다.** `"[name] walk" — [step size, arm swing]`. 이름이 움직임을 고정한다.

## 4. 눈

```text
continuous naturalistic eye life: micro-saccades and gaze targeting, the gaze drifting and settling
rather than locking, realistic blink rate tied to state, live wet catchlights, the eyes reaching
the target a beat before the head turns
```

- 인물 시트에는 눈의 물리(습기, 캐치라이트)만 넣는다. 눈의 성격은 컷 프롬프트에 넣는다.

## 5. 상태를 쓴다

영상 모델은 전환에 실패하고 상태에 성공한다. 연속 과정은 비트마다 상태로 나눠 `ACTION_TIMING` 구간에 맞춘다.

## 6. 마스터 프로필 (반복 등장 인물)

150~220단어 영어 한 문단으로, 관찰 가능한 것만 쓴다. 에셋 대장에 두고, 장면마다 그 장면의 자세·행동으로 다시 쓴다.

```text
Character acting as [NAME]. [age, build, posture]. [psychological engine, one clause].
Vocal profile: [range, accent, pace, change under pressure]. Key physical habits and tics: [tic + trigger;
stress tic + trigger; what is hidden; the mask and what breaks it]. Eye life: [§4]. Walking style:
["name" + description]. However, when [trigger], [change]. [The one thing that softens them].
```

- 모든 틱에는 방아쇠를 붙인다. 방아쇠 없는 틱은 장식이다.
- 의상, 카메라, 색은 넣지 않는다.
- 장면에서 불가능한 행동은 지우지 말고 다른 배출구로 바꾼다.

## 7. 목소리는 고정

인물마다 문장 하나를 만들어 대사가 있을 때 그대로 붙인다.

```text
"A [age]-year-old [origin/accent]. [timbre, range]; [pace, delivery]; [change under pressure]."
```

## 8. 레지스터

작품마다 "쓰는 연기 / 쓰지 않는 연기"를 `decisions.md`에 정한다. 숏이 타이트할수록 움직임을 줄인다.

## 9. 검증된 문장

| 문제 | 문장 |
|---|---|
| 감정이 넘치거나 꺼짐 | `between [A] and [B]; [extreme 1] = failed take, [extreme 2] = failed take` |
| 몸이 휙 돈다 | `head → shoulders → feet over three seconds; turning within one second = failed take` |
| 말하지 않을 인물의 입 | `no attempt to speak at all — no parted lips, no mouthing`. 망설임은 숨·삼킴·손으로 쓴다 |
| 멈춤이 놀람으로 읽힘 | `does not startle; simply stops` / `the action carries through and only the eyes stay on it` |
| 반응이 너무 크거나 없음 | `If [the reaction] is strong, it is a failed take; if there is no reaction at all, it is also a failed take.` |

## 10. 나쁜 연기 → 수정

| 증상 | 수정 |
|---|---|
| 감정을 얼굴로 묘사 | 목표와 손의 일을 준다 |
| 첫 초부터 결말을 연기 | 인물이 지금 아는 것만 쓴다 |
| 상대가 말하는 동안 빈 얼굴 | 반응이 상대 말 중간에 시작되게 한다 |
| 한 톤으로 끝까지 | 비트마다 새 전술 동사를 준다 |
| 군중이 똑같이 반응 | 어긋나게, 세기를 다르게 한다 |
| 강한 사건 뒤 즉시 회복 | 흔적이 다음 비트로 남게 한다 |
| 클로즈업에서 큰 표정 | 눈과 생각만 쓴다 |
| 죽은 눈 | §4 블록을 쓴다 |
