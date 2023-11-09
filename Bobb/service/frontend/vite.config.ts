import { defineConfig, loadEnv, UserConfigExport } from "vite";
import react from "@vitejs/plugin-react";
import tsconfigPaths from "vite-tsconfig-paths";
import svgr from "vite-plugin-svgr";

// https://vitejs.dev/config/
export default defineConfig(({ command, mode }) => {
  const env = loadEnv(mode, process.cwd(), '');

  let config: UserConfigExport ={
    plugins: [
      react(),
      tsconfigPaths(),
      svgr({ include: "**/*.svg?react", exclude: "" }),
    ],
  }

  if (mode === 'development') {
    config = {
      ...config, 
      server: {
        proxy: {
          '/api': {
            target: 'http://127.0.0.1:5000',
            changeOrigin: true,
            secure: false,
          },
        },
      }
    }
  }

  return config;
});