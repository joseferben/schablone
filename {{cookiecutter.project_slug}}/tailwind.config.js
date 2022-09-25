/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./{{cookiecutter.project_slug}}/**/*.{html,js}"],
  theme: {
    extend: {},
  },
  plugins: [require("@tailwindcss/forms")],
};
