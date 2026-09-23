/** @type {import('next').NextConfig} */
const nextConfig = {
  async rewrites() {
    // Keep browser requests same-origin in production. This avoids browser
    // privacy/network blockers while the separate FastAPI service remains the
    // actual API runtime.
    if (process.env.NODE_ENV === "production") {
      return [
        {
          source: "/api/:path*",
          destination: "https://stock-strategies-only-api.vercel.app/api/:path*",
        },
      ];
    }
    return [
      {
        source: "/api/:path*",
        destination: `${process.env.NEXT_PUBLIC_API_BASE || "http://localhost:8000"}/api/:path*`,
      },
    ];
  },
};

module.exports = nextConfig;
