import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Historia Clínica - Optometría",
  description: "Sistema de historia clínica para optometría",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="es">
      <body>{children}</body>
    </html>
  );
}
