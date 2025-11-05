// src/lib/api.js
import axios from "axios";
import { API_BASE } from "./config";

export const api = axios.create({ baseURL: API_BASE });

export const getMe = () => api.get("/me/").then(r => r.data);
export const updateMeProfile = (payload) =>
  api.post("/me/update/", payload).then(r => r.data);

export const getTips = () => api.get("/tips/").then(r => r.data);
export const listDetections = (params={}) =>
  api.get("/detections/", { params }).then(r => r.data);
