# 그림체 이미지 (수채·일러스트)

나부코 수채 배경에서 정착한 방식이다.

## 규칙

- **그림체 참조는 기법만 가져온다고 명시한다.** 이걸 빼면 참조 속 버드나무, 새, 언덕이 섞였다.
- **색 참조는 색·빛·분위기만 가져온다고 쓴다.** 풍경과 빛 방향은 가져오지 않는다.
- **표면이 돌 무늬나 타일로 읽히면** 넓은 붓 범위를 지정한다: `large, smooth, softly mottled plaster washes laid with a wide wet brush`
- **"디테일만 올려"는** 참조 하나만 넣고 "그대로 다시 그리되, 존재하는 표면의 붓터치만 더 곱게"라고 쓴다.
  - 식생을 늘리지 않는다.
  - 빛줄기를 약하게 하지 않는다.
  - 밝기는 그대로 둔다.
  - 이걸 안 쓰자 밝기, 식생, 구도까지 바뀌었다.
- **업스케일은 수채 질감을 지운다.** 큰 해상도가 필요하면 그 해상도로 생성할지 사용자에게 묻는다.
- **국소 수정은 직접 편집(픽셀 합성)이 빠르고 싸다.**
  - 대상: 하늘만 옮기기, 나무 하나 지우기, 연기 한 줄.
  - 편집본에는 "모델이 생성한 것이 아님"을 기록한다.
- **좁은 화면을 채울 때:** 이미지를 캔버스 가운데 60%로 줄여 두고 주변만 그리게 한다(`The central painting stays exactly as it is … paint only the empty margins`).
- **같은 작품 안에서는** 같은 도시, 같은 집, 같은 옷차림으로 맞춘다. 컷마다 건물 설계가 달라지지 않게 한다.

## 틀 — 그림체 장면 (참조 다섯 장)

```text
A [very loose, grainy wet-on-wet watercolor] painting on [rough cold-press paper], ultra-wide [21:9],
of the following scene.
Reference images: the first is [base cut] and sets the painting style above all ([technique]); the
second, third and fourth are further style paintings of the same kind. Take only technique, brushwork
and paper texture from these four, never their subjects, colors or composition. The fifth is [colour
cut]: take only its colors, light and mood, never its landscape and never its direction of light.
Scene: [viewpoint and angle; zones by thirds; people few and well apart].
Light: [time, sun side, shadow direction, colour range — never orange, deep or black].
Style: [surface handling — large smooth washes for walls, tiny dabs for sky]; soft lost edges, no outlines.
Look of the place: [period-accurate objects and materials; same city, same houses, same clothing as other cuts].
Composition: [crop band; occlusion zone holds only minor details; calm edges if it will be extended].
Not a photograph, 3D render, game art or detailed digital illustration; no pen outlines, vignette, text,
border, [period-wrong items].
```
