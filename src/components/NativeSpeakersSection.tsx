import Image from "next/image";

type Speaker = {
  name: string;
  description: string;
  tags: string[];
  primaryCta: { label: string; href: string };
  secondaryCta: { label: string; href: string };
  photo: { src: string; width: number; height: number; alt: string };
  bubble: { src: string; width: number; height: number; alt: string };
};

const speakers: Speaker[] = [
  {
    name: "Diego, México",
    description:
      "Aprende español conversacional con un nativo de Ciudad de México. Acento neutro, paciente y divertido — perfecto para principiantes.",
    tags: ["Principiante", "A1–A2"],
    primaryCta: { label: "Reservar clase", href: "#book-diego" },
    secondaryCta: { label: "Ver perfil", href: "#profile-diego" },
    photo: {
      src: "/images/image0_21_281.png",
      width: 1292,
      height: 975,
      alt: "Diego, profesor nativo de México",
    },
    bubble: {
      src: "/images/image1_21_281.png",
      width: 276,
      height: 211,
      alt: "Burbuja: ¡Hola!",
    },
  },
  {
    name: "Mateo, Colombia",
    description:
      "Sube tu nivel con un nativo de Bogotá. Práctica fluida, vocabulario avanzado y conversaciones reales del día a día.",
    tags: ["Avanzado", "B2–C1"],
    primaryCta: { label: "Reservar clase", href: "#book-mateo" },
    secondaryCta: { label: "Ver perfil", href: "#profile-mateo" },
    photo: {
      src: "/images/image2_21_281.png",
      width: 1049,
      height: 963,
      alt: "Mateo, profesor nativo de Colombia",
    },
    bubble: {
      src: "/images/image3_21_281.png",
      width: 187,
      height: 138,
      alt: "Estrella: ¿Listo?",
    },
  },
];

export function NativeSpeakersSection() {
  return (
    <section className="bg-cream py-16 md:py-24">
      <div className="mx-auto max-w-[1640px] px-6">
        <div className="grid grid-cols-1 gap-6 md:grid-cols-2 md:gap-10">
          {speakers.map((s) => (
            <SpeakerCard key={s.name} speaker={s} />
          ))}
        </div>
      </div>
    </section>
  );
}

function SpeakerCard({ speaker }: { speaker: Speaker }) {
  return (
    <article className="rounded-2xl bg-cream ring-1 ring-beige/60 shadow-sm p-6 md:p-8">
      <div className="grid grid-cols-1 gap-6 md:grid-cols-[1fr_1.1fr] md:gap-8">
        <div className="relative aspect-[409/356] overflow-hidden rounded-xl bg-sand">
          <Image
            src={speaker.photo.src}
            alt={speaker.photo.alt}
            fill
            sizes="(min-width: 768px) 40vw, 100vw"
            className="object-cover object-top"
            priority
          />
          <div className="absolute right-3 top-3 w-[32%] max-w-[140px]">
            <Image
              src={speaker.bubble.src}
              alt={speaker.bubble.alt}
              width={speaker.bubble.width}
              height={speaker.bubble.height}
              className="h-auto w-full drop-shadow-sm"
            />
          </div>
        </div>

        <div className="flex flex-col justify-between gap-6">
          <div>
            <h3 className="text-2xl font-semibold tracking-tight text-ink md:text-[28px]">
              {speaker.name}
            </h3>
            <div className="mt-3 flex flex-wrap gap-2">
              {speaker.tags.map((tag) => (
                <span
                  key={tag}
                  className="inline-flex h-[35px] items-center rounded-lg bg-beige px-3 text-sm font-medium text-ink"
                >
                  {tag}
                </span>
              ))}
            </div>
            <p className="mt-4 text-base leading-relaxed text-ink/80">
              {speaker.description}
            </p>
          </div>

          <div className="flex flex-col gap-3 sm:flex-row sm:items-center sm:gap-4">
            <a
              href={speaker.primaryCta.href}
              className="inline-flex h-9 items-center justify-center rounded-full bg-accent px-5 text-sm font-semibold text-white transition hover:brightness-95 focus:outline-none focus:ring-2 focus:ring-accent focus:ring-offset-2 focus:ring-offset-cream"
            >
              {speaker.primaryCta.label}
            </a>
            <a
              href={speaker.secondaryCta.href}
              className="inline-flex h-9 items-center justify-center rounded-full border border-ink/15 bg-transparent px-5 text-sm font-semibold text-ink transition hover:bg-ink/5"
            >
              {speaker.secondaryCta.label}
            </a>
          </div>
        </div>
      </div>
    </article>
  );
}
