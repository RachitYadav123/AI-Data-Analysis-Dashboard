:root {
  --bg: #0f172a;
  --panel: #ffffff;
  --muted: #64748b;
  --line: #e2e8f0;
  --brand: #2563eb;
  --brand-dark: #1e40af;
}
* { box-sizing: border-box; }
body.site-body { background: #f8fafc; color: #0f172a; font-family: Inter, ui-sans-serif, system-ui, -apple-system, Segoe UI, Arial, sans-serif; }
.app-nav { background: linear-gradient(135deg, #0f172a, #1e3a8a); }
.landing-hero { background: white; border: 1px solid var(--line); border-radius: 24px; padding: 48px; box-shadow: 0 20px 60px rgba(15, 23, 42, 0.08); }
.landing-hero h1 { max-width: 920px; font-size: clamp(2rem, 4vw, 4rem); letter-spacing: -0.04em; font-weight: 800; }
.eyebrow { text-transform: uppercase; color: var(--brand); font-weight: 800; letter-spacing: 0.12em; }
.auth-card { max-width: 460px; margin: 40px auto; padding: 32px; background: white; border: 1px solid var(--line); border-radius: 20px; box-shadow: 0 20px 60px rgba(15, 23, 42, 0.08); }
.dash-shell { min-height: 100vh; background: #f1f5f9; padding: 18px; }
.hero-panel { background: linear-gradient(135deg, #0f172a, #1d4ed8); color: white; border-radius: 24px; padding: 26px; box-shadow: 0 24px 70px rgba(37, 99, 235, 0.25); }
.brand-line { font-size: 2rem; font-weight: 800; letter-spacing: -0.03em; }
.brand-line span { background: white; color: #1d4ed8; border-radius: 10px; padding: 0 10px; margin-right: 6px; }
.top-actions { display: flex; justify-content: flex-end; gap: 8px; align-items: center; height: 100%; }
.panel-card { border: 1px solid var(--line); border-radius: 18px; box-shadow: 0 14px 40px rgba(15, 23, 42, 0.06); }
.panel-card h5 { font-weight: 800; margin-bottom: 14px; }
.upload-box { border: 2px dashed #93c5fd; border-radius: 16px; padding: 28px 16px; text-align: center; background: #eff6ff; cursor: pointer; }
.status-text { color: var(--muted); font-size: 0.9rem; }
.kpi-grid { display: grid; grid-template-columns: repeat(6, minmax(120px, 1fr)); gap: 12px; }
.kpi-card { background: white; border: 1px solid var(--line); border-radius: 16px; padding: 14px; box-shadow: 0 10px 30px rgba(15, 23, 42, 0.05); }
.kpi-card small { display: block; color: var(--muted); font-weight: 700; }
.kpi-card strong { display: block; font-size: 1.4rem; margin-top: 4px; }
.chart-row .js-plotly-plot { background: white; border: 1px solid var(--line); border-radius: 18px; box-shadow: 0 10px 30px rgba(15, 23, 42, 0.05); }
.insight-list { padding-left: 18px; }
.insight-list li { margin-bottom: 8px; }
.profile-box { font-size: 0.95rem; line-height: 1.8; }
.ai-summary { background: #f8fafc; border: 1px solid var(--line); border-radius: 12px; padding: 12px; white-space: pre-wrap; max-height: 260px; overflow: auto; }
.custom-input { width: 100%; min-height: 88px; border: 1px solid #cbd5e1; border-radius: 12px; padding: 10px; }
.DateRangePickerInput, .SingleDatePickerInput { border-radius: 10px; border-color: #cbd5e1; }
@media (max-width: 1200px) { .kpi-grid { grid-template-columns: repeat(3, 1fr); } }
@media (max-width: 768px) { .kpi-grid { grid-template-columns: repeat(2, 1fr); } .top-actions { justify-content: flex-start; } .landing-hero { padding: 28px; } }
