import react from '@vitejs/plugin-react'
import { defineConfig } from 'vite'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  // Always use port 5173 (the backend's CORS only allows 5173).
  // strictPort: if 5173 is busy, stop with an error instead of jumping to 5174.
  server: { port: 5173, strictPort: true },
})
