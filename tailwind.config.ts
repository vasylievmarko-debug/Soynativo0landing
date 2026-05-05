import type { Config } from "tailwindcss";

const config: Config = {
  content: ["./src/**/*.{js,ts,jsx,tsx,mdx}"],
  theme: {
    extend: {
      colors: {
        cream: "#FEFAF5",
        ink: "#141E25",
        accent: "#E8511B",
        sage: "#EAEBD8",
        sand: "#EBE2DB",
        beige: "#EFE6E0",
        gold: "#FAE9C4",
      },
      fontFamily: {
        sans: ["var(--font-inter)", "system-ui", "sans-serif"],
      },
    },
  },
  plugins: [],
};

export default config;
