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

### Completed Enhancements

- Moved scene data into `scene_config.json`.
- Added structured logging with information, warning, and error messages.
- Added validation for configuration values and resource paths.
- Added safe fallback behavior for missing textures.
- Replaced inline rendering logic with named private helpers.

### Artifact Files

- [Original SceneManager.cpp](artifacts/cs330-opengl-castle-scene/original/SceneManager.cpp)
- [Enhanced Logger.h](artifacts/cs330-opengl-castle-scene/enhanced/Logger.h)
- [Enhanced scene_config.json](artifacts/cs330-opengl-castle-scene/enhanced/scene_config.json)
- [Web enhancement narrative](artifacts/cs330-opengl-castle-scene/narrative)

### Course Outcome Alignment

**Outcome 4:** The enhancement uses data-driven configuration, structured logging, and modular rendering helpers to improve maintainability and extensibility.

**Outcome 5:** Validation, safe resource handling, pointer checks, and fallback texture behavior reduce the risk of undefined behavior and improve reliability.

[Back to portfolio home](./)
