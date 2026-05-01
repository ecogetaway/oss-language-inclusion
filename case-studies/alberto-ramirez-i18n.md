# Case Study: i18n Workflow in Video Games and Web Development

**Contributor:** Alberto Ramirez

**Context:** Professional experience in localization for gaming and full-stack web applications.

## Overview
In industries like video games and professional web apps, the localization (i18n) process is often managed through structured asset pipelines to ensure consistency across languages.

## The Pattern: JSON Dictionary Strategy
The most consistent pattern observed is the use of structured JSON dictionaries as the source of truth.

### 1. File Structure
The project maintains a single source of truth for keys, with separate files for each locale:
- `en.json` (Source)
- `es.json` (Target)

### 2. Implementation Example
Keys are used as constants in the code to prevent UI breakage when translations are updated.

```json
{
  "menu": {
    "home": "Home",
    "settings": "Settings",
    "logout": "Log Out"
  }
}
```

### Review & Workflow
Based on my experience, the review process varies by project scale:

- Large Scale (Video Games): Translations are usually handled by external agencies. Review is conducted by native QA testers who verify cultural context and UI overflow (text fitting).

- Small/Ad Hoc Projects: Developers manage JSON files manually, often using automated translation tools as a baseline followed by manual peer reviews.

### Observed Challenges & Friction
* **Key Ambiguity:** Using generic or highly similar keys (e.g., `button_save` vs `save_label`) often leads to accidental reuse. 
* **Context Loss:** Reusing a key in different UI sections saves time initially but creates issues later; changing the text for one specific use case might inadvertently break another section of the app.
* **Dictionary Bloat:** Without a strict naming convention, it becomes difficult for maintainers to identify if a key is still in use or redundant, increasing the risk of "dead" translation strings.

### Conclusion
Observations across projects suggest that while key-based JSON management is the industry standard, its success depends on strict governance. Standardizing the naming conventions early—rather than relying on ad hoc workarounds—significantly reduces the maintainer's workload and prevents technical debt as the application scales.