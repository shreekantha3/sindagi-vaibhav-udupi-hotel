# TEST REPORT — Vaibhav Udupi Hotel
> Date: 2026-09-10 | Tester: Senior Engg | Segment: Food | Tier-2 (no phone in CSV)

## Build
- [x] `npm run build` PASS (vite 5.4.21, 4 modules, 0 warnings)
- dist sizes: 12.62 kB HTML / 12.49 kB CSS / 1.20 kB JS — well under perf budget (<200KB JS, <1.5MB total)
- dist base paths verified: `/sindagi-vaibhav-udupi-hotel/assets/*` + favicon.svg copied

## Static checks (all PASS)
- [x] NO tel:/wa.me/+91 anywhere (grep CLEAN) — CSV phone empty, never invented
- [x] Directions/Maps CTAs only: nav, hero, visit, mobile floating button all → Google Maps URL
- [x] data-missing flag present (2× `data-missing="phone..."` — hero banner + visit note)
- [x] JSON-LD Restaurant + servesCuisine South Indian (no telephone key) + AggregateRating 4.0
- [x] H1 South-Indian meals angle, semantic sections, skip link, async fonts (media=print onload)
- [x] No lorem ipsum, no invented hours/prices (in-store/on-visit fallback)
- [x] aria-expanded on nav toggle, keyboard reachable CTAs, contrast-safe palette (pilot copy)

## Pending (requires preview + device lab before Deployed)
- [ ] Lighthouse CI mobile+desktop (target 90/95/95/95)
- [ ] Playwright 12-case E2E + axe (0 serious) + linkinator
- [ ] Screenshots 360/768/1440 attached to PR
- [ ] GitHub Pages deploy verify (200 + base path assets)

## Verdict: BUILT + STATIC QA PASS → ready for full QA + separate repo deploy
