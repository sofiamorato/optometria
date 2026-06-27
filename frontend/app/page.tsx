/**
 * Página temporal de verificación.
 *
 * No es una pantalla del producto final (login, búsqueda de pacientes, etc.).
 * Su único propósito en esta fase es confirmar que el frontend puede
 * comunicarse con el backend (FastAPI) a través de NEXT_PUBLIC_API_URL.
 *
 * Las pantallas reales se construirán en la Fase 2 (ver GUIA_DESARROLLO.md).
 */
import { checkBackendHealth } from "@/lib/api";

export default async function Home() {
  const health = await checkBackendHealth();

  return (
    <main className="flex min-h-screen flex-col items-center justify-center gap-4 p-8 text-center">
      <h1 className="text-3xl font-semibold text-primary">
        Optometría — Estructura inicial
      </h1>
      <p className="text-muted-foreground">
        Esta pantalla es solo de verificación de conexión con el backend.
      </p>
      <div className="rounded-lg border border-border bg-secondary px-6 py-4">
        <p>
          Estado del backend:{" "}
          <span className="font-medium">
            {health ? `${health.api} / BD: ${health.base_de_datos}` : "sin conexión"}
          </span>
        </p>
      </div>
    </main>
  );
}
