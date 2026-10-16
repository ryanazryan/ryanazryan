# Validation record

Executed locally on 16 October 2026. No repository was modified, pushed, or deployed.

## Game — executed in Chromium

- Complete keyboard playthrough: three module pickups, two correct bug fixes, workstation win state.
- A deliberately wrong puzzle answer kept progress unchanged, showed retry feedback, and allowed a correct answer afterward.
- Complete text-mode playthrough using labelled destination and answer buttons.
- Visiting the workstation before completing tasks did not win or advance progress.
- Both the win-screen replay and Restart project reset progress correctly.
- Mobile touch movement and interaction collected a module successfully.
- Reduced-motion browser emulation enabled Quiet motion by default.
- Local `file://` loading, starting the game and collecting a module worked; no backend was required.
- Desktop layout inspected at 1440 px; mobile layout inspected at 390 px and 320 px. No horizontal overflow. Touch controls were moved immediately beneath the room after visual review.
- Final tested gameplay run produced zero JavaScript/page errors and zero console errors. A missing favicon found in the first pass was corrected.
- No loss state is intended: there is no timer, damage, or permanent penalty. Puzzles can be retried. The final “deployment” affects only local game state.

## Artwork and README

- Every shipped SVG was parsed as XML and rasterized successfully. All 17 README SVG assets include title/description and outlined text; the standalone favicon is the 18th SVG.
- No asset SVG depends on a remote image, installed font, script, or external stylesheet. Raster scene inputs are embedded in the composition SVGs.
- Original hero, all four project compositions, mobile variants, game preview, toolkit, achievement shelf and contribution garden were rendered and inspected. Text has been enlarged in mobile project variants.
- The README was rendered through a local GitHub-Flavored-Markdown renderer with a GitHub-like stylesheet at desktop width, 390 px, and dark mode. Mobile `picture` sources were selected correctly. This is a **local approximation**, not a claim that the new README was uploaded to or rendered by GitHub.
- Local image, CSS, font, Markdown and HTML file references were checked. No referenced asset is missing in the delivered archive.
- The README contains no JavaScript, iframe, custom CSS, or fake live game link. The preview opens the included source until Pages is manually enabled and checked.
- The hero has a static complete composition and a subtle SVG lamp-light animation with a reduced-motion rule. Individual GitHub image proxies/renderers may show the static frame.

## Evidence and integrity

- Current repository manifests, file trees and selected implementation files were inspected; evidence is linked in [VERIFICATION.md](VERIFICATION.md).
- Pull Shark ×2, Pair Extraordinaire, YOLO and Quickdraw were checked in the live GitHub achievement view. Illustrations are explicitly unofficial.
- Contribution source data contains **289 unique consecutive dates**, 1 January–16 October 2026. Counts sum to **185**, across **53 days** with activity. Future dates returned in GitHub's calendar response were excluded. Column heights use the original 0–4 intensity values.
- The contribution fetcher validates dates, levels, counts, uniqueness, and completeness before replacing data. Generated README statistics and SVG values share the same JSON input.
- JavaScript syntax, Python syntax, bundled font licenses, and SVG XML were checked. All three font license files identify SIL OFL 1.1.
- No credential, API key, environment file, custom workflow, publishing script, or runtime package dependency is required.

## Limits

- Featured project repositories were inspected, not compiled or executed. Their production readiness is not claimed.
- Pages setup and the live play URL remain unverified because deployment was intentionally left to the owner.
- LinkedIn and Instagram ownership links match the live profile; their authenticated destination contents were not inspected. YouTube channel and both selected video titles were verified live. Discord invite validity remains unverified.
- Browser testing used Chromium on Windows with emulated mobile dimensions and touch. Safari, Firefox, physical mobile devices and assistive technology sessions were not separately tested. Accessibility features were implemented and exercised through keyboard and text mode; this is not a formal accessibility certification.
