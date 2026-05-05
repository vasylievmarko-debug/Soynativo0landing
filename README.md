# Soy Nativo — Landing

Лендинг для сервиса изучения испанского с носителями языка.
Стек: **Next.js 14 (App Router) + TypeScript + Tailwind CSS**.

## Запуск

```bash
npm install
npm run dev
```

Открой http://localhost:3000

## Структура

- `src/app/` — страницы (App Router)
- `src/components/NativeSpeakersSection.tsx` — секция «Двое нативных носителей»
- `public/images/` — изображения, извлечённые из Figma SVG
- `design/right-section-1.svg` — оригинальный Figma экспорт

## Секция NativeSpeakersSection

Воспроизводит блок из `design/right-section-1.svg`:
- Две карточки рядом (на мобиле — вертикально)
- В каждой: фото нативного носителя + speech-bubble
- Имя, теги уровня (CEFR), описание, две CTA-кнопки

Тексты внутри карточек — заглушки. Замени `speakers` в
`src/components/NativeSpeakersSection.tsx` на реальные данные из Figma.
