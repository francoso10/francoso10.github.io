# CS 330 OpenGL Castle Scene - Enhancement Narrative

## Artifact Description

The selected artifact is my final project from CS 330: Computational Graphics and Visualization. It is a three-dimensional castle scene built with C++, OpenGL, GLFW, GLEW, and GLM. The scene includes towers, walls, a front door, topiary shapes, lamps, texture mapping, lighting, and WASD plus mouse-based navigation.

The original project rendered correctly but depended on hardcoded values for object positions, textures, materials, and lighting inside `SceneManager.cpp`. Changes required editing source code and recompiling the project.

## Enhancement Description

I enhanced the scene-management component through four major improvements. First, I moved scene data, including textures, materials, lighting, object positions, and scales, into `scene_config.json`. The enhanced SceneManager loads this data at runtime, separating scene data from rendering logic.

Second, I added a structured `Logger` class with information, warning, and error messages. This provides consistent diagnostic output and makes troubleshooting more readable.

Third, I applied defensive programming by validating JSON access and file paths and by providing safe fallback behavior for missing textures. These checks reduce the likelihood of crashes or undefined rendering behavior.

Finally, I replaced inline rendering logic with named helpers such as `DrawTopiaryBall` and `DrawLamp`. This improves readability, reuse, and maintainability.

## Course Outcome Alignment

This enhancement supports Outcome 4 through JSON-driven configuration, structured logging, and modular organization. It supports Outcome 5 through validation, safe resource handling, pointer checks, and fallback behavior that keeps the renderer in a defined state.

## Reflection

The most significant design decision was determining which information belonged in external configuration and which values should remain in C++ implementation logic. I learned to distinguish scene data, such as object positions and UV tiling, from mesh-specific rendering details. I also gained a stronger understanding of OpenGL error-state behavior and compatibility concerns involving existing classes that use raw pointers without internal safeguards.
