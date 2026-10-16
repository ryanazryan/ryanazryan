# Source verification — Ryan’s Creative Engineering Studio

Checked on 2026-10-16 (Asia/Makassar). Read-only inspection; no repositories, deployments, account settings, social content, or external records were modified. This is evidence for copywriting, not a runtime/security audit of the featured projects.

## Method and freshness

- Repository metadata, recursive main-branch file trees, manifests, and selected implementation files were fetched directly through the connected GitHub connector during this task.
- Branch references were fetched separately. Snapshot commits are listed below.
- A general web fetch of the GitHub profile returned a cached result explicitly labelled “Crawled: 1.2 years ago.” That cached result was **not** used to claim current achievement tiers.
- The actual public achievement page was subsequently opened successfully in the live browser. Its current “Earned achievements” section confirmed all four names and the Pull Shark x2 label.
- Direct shell HTTP could not resolve github.com during the initial delegated inspection. Browser and connector reads supplied the repository and achievement evidence. After network permission was granted, a separate direct HTTP fetch supplied the public contribution-calendar snapshot described below.

| Repository | Branch | Snapshot commit |
|---|---|---|
| [ryanazryan](https://github.com/ryanazryan/ryanazryan) | main | [5e42a8b65b61](https://github.com/ryanazryan/ryanazryan/commit/5e42a8b65b6160a729ab3e7cffbadf391a0387d1) |
| [auvrion-biosphere](https://github.com/ryanazryan/auvrion-biosphere) | main | [2b103019b8d6](https://github.com/ryanazryan/auvrion-biosphere/commit/2b103019b8d624008b2eb009506431c993bbdd23) |
| [ruma](https://github.com/ryanazryan/ruma) | main | [39442f96dab8](https://github.com/ryanazryan/ruma/commit/39442f96dab8a4d8ce8ee5d3749b994b3f9b31ae) |
| [Hydropedia](https://github.com/ryanazryan/Hydropedia) | main | [6939a46ce997](https://github.com/ryanazryan/Hydropedia/commit/6939a46ce997cf4134f65613fe5d6a6c8496c0fe) |
| [sena](https://github.com/ryanazryan/sena) | main | [20b5edab5d2b](https://github.com/ryanazryan/sena/commit/20b5edab5d2b14b28ea7d5d6f57d9c9748c9d58f) |

## Existing profile README

Source: [current README](https://github.com/ryanazryan/ryanazryan/blob/5e42a8b65b6160a729ab3e7cffbadf391a0387d1/README.md).

It contains the supplied Discord, Instagram, LinkedIn and YouTube destinations, both supplied historical YouTube videos, technology icon collections, an external trophy service, an external streak service, and a third-party lofi GIF. It contains no original asset directory in the inspected main tree. Existing skill declarations may be retained as the owner’s self-description, but do not establish expert proficiency or production experience. The previous profile-view image uses a different username; do not copy that counter.

## Auvrion Biosphere

**Recommended concise copy:** “Environmental intelligence groundwork for biodiversity observations, forest-fire risk monitoring and WebGIS.”

**Maturity:** “Early development” or “Foundation in progress.” Do not present the environmental product capabilities as implemented, verified, deployed or production-ready.

**Confirmed technology:** Next.js, React, TypeScript, Drizzle ORM, PostgreSQL, Better Auth; local Docker Compose selects a PostGIS image. Tailwind is a declared development dependency. MapLibre is proposed in the README but absent from the inspected package manifest.

**Implementation evidence:**
- [package.json](https://github.com/ryanazryan/auvrion-biosphere/blob/2b103019b8d624008b2eb009506431c993bbdd23/package.json): Next.js/React, pg, Drizzle and Better Auth dependencies.
- [server authentication](https://github.com/ryanazryan/auvrion-biosphere/blob/2b103019b8d624008b2eb009506431c993bbdd23/src/server/auth/index.ts): Better Auth configured with a Drizzle PostgreSQL adapter.
- [compose.dev.yml](https://github.com/ryanazryan/auvrion-biosphere/blob/2b103019b8d624008b2eb009506431c993bbdd23/compose.dev.yml): PostGIS database service.
- [home page](https://github.com/ryanazryan/auvrion-biosphere/blob/2b103019b8d624008b2eb009506431c993bbdd23/src/app/page.tsx): “Application initialization in progress.”
- Recursive tree contains auth, health, account, authorization, and database modules/migrations; the visible main tree does not implement the proposed environmental observation interface.
- [README](https://github.com/ryanazryan/auvrion-biosphere/blob/2b103019b8d624008b2eb009506431c993bbdd23/README.md) explicitly describes an initial-development competition prototype and says planned features are not completed/tested.

## Ruma Marketplace

**Recommended concise copy:** “Commerce platform groundwork, with a planned Next.js and NestJS architecture.”

**Maturity:** “Architecture & workspace setup.” Do not list implemented catalog, inventory, checkout, payments, shipping or admin features.

**Critical distinction:** The repository is named ruma, but its current README title and root package name use “Moorlife Marketplace.” Keeping the requested portfolio title “Ruma Marketplace” is reasonable; do not invent a different shipped product.

**Confirmed implementation:** A pnpm workspace root. The complete current main tree has only .gitignore, README.md, package.json and pnpm-workspace.yaml. No apps/frontend, apps/backend, packages or other application source directories are present, despite the README’s proposed tree.

**Planned technology only:** Next.js, React, TypeScript, Tailwind, NestJS, Prisma, PostgreSQL and Redis. External services named in the README are plans, not proven integrations.

Sources:
- [README](https://github.com/ryanazryan/ruma/blob/39442f96dab8a4d8ce8ee5d3749b994b3f9b31ae/README.md)
- [root package](https://github.com/ryanazryan/ruma/blob/39442f96dab8a4d8ce8ee5d3749b994b3f9b31ae/package.json)
- [workspace declaration](https://github.com/ryanazryan/ruma/blob/39442f96dab8a4d8ce8ee5d3749b994b3f9b31ae/pnpm-workspace.yaml)
- [complete tree API](https://api.github.com/repos/ryanazryan/ruma/git/trees/39442f96dab8a4d8ce8ee5d3749b994b3f9b31ae?recursive=1)

## Hydropedia

**Recommended concise copy:** “An academic hydroponic plant-management app with pH and nutrient monitoring views.”

**Maturity:** “Academic project.” Functionality is present in source; this task did not compile or run this repository.

**Current stack:** Java 17, Spring Boot, Spring MVC, Thymeleaf, SQLite, Maven and Spring Data JPA. Do **not** describe the current UI as JSP. The source and manifest now use Thymeleaf. The README’s Spring Boot version description differs from the pom.xml; omit exact version numbers from the portfolio.

**Implementation evidence:**
- [pom.xml](https://github.com/ryanazryan/Hydropedia/blob/6939a46ce997cf4134f65613fe5d6a6c8496c0fe/pom.xml): Java 17, Spring Boot, webmvc, thymeleaf, data-jpa and sqlite-jdbc.
- [plant controller](https://github.com/ryanazryan/Hydropedia/blob/6939a46ce997cf4134f65613fe5d6a6c8496c0fe/src/main/java/com/hydropedia/hydropedia/controller/TanamanController.java): plant create/read/update/delete operations.
- [view controller](https://github.com/ryanazryan/Hydropedia/blob/6939a46ce997cf4134f65613fe5d6a6c8496c0fe/src/main/java/com/hydropedia/hydropedia/controller/ViewController.java): dashboard, plants, monitoring and notifications templates.
- [monitoring controller](https://github.com/ryanazryan/Hydropedia/blob/6939a46ce997cf4134f65613fe5d6a6c8496c0fe/src/main/java/com/hydropedia/hydropedia/controller/MonitoringController.java) and [service](https://github.com/ryanazryan/Hydropedia/blob/6939a46ce997cf4134f65613fe5d6a6c8496c0fe/src/main/java/com/hydropedia/hydropedia/service/MonitoringService.java): pH/nutrient status checking and a basic in-memory log.
- [README](https://github.com/ryanazryan/Hydropedia/blob/6939a46ce997cf4134f65613fe5d6a6c8496c0fe/README.md) identifies a team object-oriented-programming assignment. Do not imply sole authorship or verified live sensor ingestion.

## SENA Education

**Recommended concise copy:** “A literacy-learning application with student and teacher views, submissions and feedback integrations.”

**Maturity:** “Learning-platform project.” Source is implemented, but live backend integration and production operation were not tested in this task.

**Confirmed stack:** React, TypeScript, Vite, Firebase Authentication/Firestore, Node.js/Firebase Functions. Root package contains React and Vite; .tsx source confirms TypeScript. The project is not best described as a Next.js application merely because Next appears among development dependencies.

**Implementation evidence:**
- [package.json](https://github.com/ryanazryan/sena/blob/20b5edab5d2b14b28ea7d5d6f57d9c9748c9d58f/package.json): React, Firebase, Vite, scripts invoking Vite.
- [App.tsx](https://github.com/ryanazryan/sena/blob/20b5edab5d2b14b28ea7d5d6f57d9c9748c9d58f/src/App.tsx): login/register flow and role-specific student/teacher dashboards.
- [auth.ts](https://github.com/ryanazryan/sena/blob/20b5edab5d2b14b28ea7d5d6f57d9c9748c9d58f/src/lib/auth.ts): Firebase email/password and Google sign-in with Firestore profile operations.
- [GamesSection.tsx](https://github.com/ryanazryan/sena/blob/20b5edab5d2b14b28ea7d5d6f57d9c9748c9d58f/src/components/GamesSection.tsx): Firestore game-submission collection operations, screenshot upload code, grading/rejection UI and backend feedback requests.
- [Firebase Functions source](https://github.com/ryanazryan/sena/blob/20b5edab5d2b14b28ea7d5d6f57d9c9748c9d58f/functions/src/index.ts): Express feedback endpoint integrating GoogleGenAI and user-cleanup handler.
- [README](https://github.com/ryanazryan/sena/blob/20b5edab5d2b14b28ea7d5d6f57d9c9748c9d58f/README.md) still labels role management and progress tracking as future ideas despite role-related code. Prefer source-backed, narrow claims and avoid declaring every roadmap feature complete. No claims about scalability or guaranteed AI service availability.

## Achievements — live verified

Live URL: [GitHub earned achievements](https://github.com/ryanazryan?tab=achievements).

The live browser accessibility tree displayed the following inside “Earned achievements” on 2026-10-16:

- Pull Shark — **x2** displayed.
- Pair Extraordinaire — earned; no multiplier shown.
- YOLO — earned; no multiplier shown.
- Quickdraw — earned; no multiplier shown.

The same names also appear in the profile sidebar. Do not infer contribution totals, merged-PR counts, or unshown tiers from these labels. Custom studio-themed illustrations should say they are unofficial artwork. Use the live profile link for readers to see GitHub’s original badges.

## Social and video links

- [LinkedIn](https://linkedin.com/in/naufalazryan): destination matches both the current README and live GitHub profile. Independent destination access through web fetch returned a cache miss; profile ownership link verified, LinkedIn page contents not checked.
- [Instagram](https://instagram.com/naufalazryan): destination matches both the current README and live GitHub profile. Independent web fetch returned a cache miss; profile ownership link verified, Instagram page contents not checked.
- [Discord](https://discord.gg/naufalazryan): preserved from user input and current README. Invite validity remains unverified. Live browser navigation was rejected by the origin approval gate with “user declined permission.” No alternate route or workaround was attempted.
- [YouTube channel](https://www.youtube.com/@naufalazryan): live browser opened successfully and showed the channel “Ryan” with the expected handle.
- [Konsep Dasar Basis Data](https://www.youtube.com/watch?v=2Y-i05hqKXg): live browser opened successfully; player showed 2:50 duration and channel link @naufalazryan.
- [Video HEI Telkom University](https://www.youtube.com/watch?v=GnV00HJbsH8): live browser opened successfully; current heading and author Ryan/@naufalazryan verified, 5:22 player duration.
- Neither video should be labelled “latest.” Preserve as selected videos or a compact “from my notebook” feature.

## Scope limitations

### Contribution artwork

The public [GitHub calendar endpoint](https://github.com/users/ryanazryan/contributions?from=2026-01-01&to=2026-10-16) was fetched directly. GitHub returned the 2026 calendar; only dates from 1 January through 16 October 2026 were retained. The included [JSON snapshot](design/contributions.json) records 289 dates, each original intensity level and the count from the corresponding GitHub tooltip. Their counts total 185 and 53 dates have nonzero activity. These are publicly visible calendar values, subject to GitHub's visibility rules, not invented metrics or a guarantee of complete private activity. The graph is a dated snapshot and its heights encode intensity levels, not linear contribution counts.

Repository inspection was read-only and selective. No code was executed from these repositories, no deployments were validated, no account was signed into, and no social interaction was performed. Existing statistics services in the old README were observed as URLs only; their live availability and metrics were not verified. Use only a generated activity asset with explicit snapshot dates and provenance or a direct profile link, rather than inventing statistics.

