import axios from "axios";

// Dev uses Vite proxy → '/api'. Prod can set VITE_API_URL='https://api.yourdomain.com/api'
const baseURL = import.meta.env.VITE_API_URL || "/api";

export const api = axios.create({ baseURL });

// --- endpoints ---
export const ping            = () => api.get("/ping/");
export const getTips         = () => api.get("/tips/");
export const getWeather      = () => api.get("/weather/");
export const getAir          = () => api.get("/air/");
export const listDetections  = () => api.get("/detections/");

export const inferImage = (file) => {
  const form = new FormData();
  form.append("image", file);
  return api.post("/infer/", form, {
    headers: { "Content-Type": "multipart/form-data" },
  });
};
