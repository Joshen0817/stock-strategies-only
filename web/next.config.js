/** @type {import('next').NextConfig} */
const nextConfig = {
  async rewrites() {
    // Local development uses the FastAPI dev server. In production Vercel
    // routes /api/* to the Python function configured in the repo root.
    if (process.env.NODE_ENV === "production") return [];
    return [
      {
        source: "/api/:path*",
        destination: `${process.env.NEXT_PUBLIC_API_BASE || "http://localhost:8000"}/api/:path*`,
      },
    ];
  },
};

module.exports = nextConfig;
