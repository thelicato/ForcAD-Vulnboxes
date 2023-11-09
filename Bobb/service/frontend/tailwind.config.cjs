/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{js,jsx,ts,tsx}"],
  theme: {
    extend: {
      colors: {
        cYellow: "#ffc245",
        cGreen: "#01a081",
        cBlack: "#1d1d1d",
      },
      fontFamily: {
        Jost: ["Jost", "sans-serif"],
        Bungee: ["Bungee Inline", "sans-serif"],
        Belanosima: ["Belanosima", "sans-serif"],
      },
    },
  },
  plugins: [require("@tailwindcss/typography"), require("daisyui")],
  daisyui: {
    themes: ["light", "dark"],
  },
};
