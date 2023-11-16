import '@/app/ui/global.css';
import { poppins } from './ui/fonts';

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className={`${poppins.className} antialiased`}>
        {children}
        <h1 className='text-blue-500'>Hola a todos</h1>
        <footer className='py-10 flex justify-center items-center'>Hecho con 💙 por la gente de vercel</footer>
      </body>
    </html>
  );
}
