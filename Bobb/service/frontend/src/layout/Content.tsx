export const Content: React.FC<React.BaseHTMLAttributes<HTMLDivElement>> = ({
  children,
}: React.BaseHTMLAttributes<HTMLDivElement>) => {
  return <main className="mb-8">{children}</main>
}