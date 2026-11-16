const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1400, height: 1000 } });
  const html = require('fs').readFileSync(process.argv[2], 'utf8');
  await p.setContent('<!doctype html><meta charset="utf-8">' + html, { waitUntil: 'networkidle', timeout: 60000 }).catch(()=>{});
  await p.emulateMedia({ colorScheme: 'light' });
  await p.addStyleTag({ content: `
    body{padding:0 !important}
    .wrap{max-width:none;gap:18px}
    .grid{grid-template-columns:repeat(3,1fr) !important;gap:10px}
    .cut{break-inside:avoid;page-break-inside:avoid}
    .seq{break-before:page} .seq:first-of-type{break-before:auto}
    .seq h2{break-after:avoid}` });
  await p.evaluate(() => document.fonts.ready);
  await p.pdf({ path: process.argv[3], format: 'A4', landscape: true, printBackground: true,
    margin: { top: '12mm', bottom: '12mm', left: '10mm', right: '10mm' },
    displayHeaderFooter: true, headerTemplate: '<span></span>',
    footerTemplate: '<div style="font-size:8px;width:100%;text-align:center;color:#888">광야 수업 #1 인트로 콘티 · <span class="pageNumber"></span>/<span class="totalPages"></span></div>' });
  await b.close();
})();
