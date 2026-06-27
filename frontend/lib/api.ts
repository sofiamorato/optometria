/**
 * Cliente mínimo para conectar el frontend con el backend FastAPI.
 *
 * Se ampliará en las siguientes fases con funciones para autenticación,
 * pacientes, consultas y documentos.
 */

export const API_URL = process.env.NEXT_PUBLIC_API_URL ?? "http://localhost:8000";

export interface HealthResponse {
  api: string;
  base_de_datos: string;
}

export async function checkBackendHealth(): Promise<HealthResponse | null> {
  try {
    const res = await fetch(`${API_URL}/health`, { cache: "no-store" });
    if (!res.ok) return null;
    return (await res.json()) as HealthResponse;
  } catch {
    return null;
  }
}
