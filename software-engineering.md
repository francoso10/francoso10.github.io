---
layout: default
title: Software Engineering and Design
---

# Software Engineering and Design

## CS 330 OpenGL Castle Scene

**Language and tools:** C++, OpenGL, GLFW, GLEW, GLM, and JSON for Modern C++  
**Category:** Software Engineering and Design

### Artifact Overview

This artifact is an interactive three-dimensional castle scene created for CS 330: Computational Graphics and Visualization. The original application renders towers, walls, a front door, topiary shapes, and lamps with texture mapping, lighting, and WASD plus mouse-based camera navigation.

The original scene functioned correctly, but much of the scene configuration and rendering behavior depended on hardcoded values inside the SceneManager. Changes to textures, materials, object placement, lighting, or scale required editing C++ source code and recompiling the application.

### Enhancement Goal

The enhancement focused on making the scene-management system more maintainable, reliable, and data-driven. Rather than treating scene data as fixed code, the enhanced implementation separates scene configuration from rendering behavior and adds safeguards for external resources.

### Completed Enhancements

- Moved scene data such as textures, materials, lighting, object positions, and scales into `scene_config.json`.
- Added structured logging with clear information, warning, and error messages.
- Added validation for configuration values and resource paths.
- Added safe fallback handling for missing textures so the renderer remains in a defined state.
- Replaced inline rendering logic with named private helpers, including reusable functions for scene elements such as lamps and topiary shapes.

### Skills Demonstrated

- Data-driven software design
- Separation of configuration from implementation
- Maintainable C++ organization
- Defensive programming and resource validation
- Logging and troubleshooting practices
- Low-level graphics and rendering-system reasoning

### Course Outcome Alignment

**Outcome 4: Innovative techniques, skills, and tools.** The enhancement applies JSON-based configuration, structured logging, and modular rendering helpers to produce a more maintainable and extensible application.

**Outcome 5: Security mindset.** Validation of external configuration, safe file handling, pointer checks, and fallback texture behavior reduce the risk of undefined behavior and improve the reliability of the renderer.

### Portfolio Materials

The final portfolio package will include the original source, enhanced source, configuration file, and enhancement narrative for this artifact.

[Back to portfolio home](./)
