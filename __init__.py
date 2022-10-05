bl_info = {
    "name": "Stable Diffusion Render",
    "description": "Use the Stable Diffusion AI algorithm to create a new image based on your render and a text prompt",
    "author": "Ben Rugg",
    "version": (0, 1, 0),
    "blender": (3, 3, 0),
    "location": "3D View > Sidebar  &  Render Properties > Stable Diffusion Render",
    "warning": "",
    "tracker_url": "",
    "category": "Render",
}


if "bpy" in locals():
    import imp
    imp.reload(config)
    imp.reload(constants)
    imp.reload(handlers)
    imp.reload(operators)
    imp.reload(preferences)
    imp.reload(properties)
    imp.reload(task_queue)
    imp.reload(ui_panels)
    imp.reload(ui_preset_styles)
    imp.reload(utils)
else:
    from . import (
        config,
        constants,
        handlers,
        operators,
        preferences,
        properties,
        task_queue,
        utils,
    )
    from .ui import (
        ui_panels,
        ui_preset_styles,
    )

import bpy


def register():
    handlers.register_handlers()
    operators.register_operators()
    preferences.register_preferences()
    properties.register_properties()
    task_queue.register_task_queue()
    ui_panels.register_ui_panels()
    ui_preset_styles.register_ui_preset_styles()


def unregister():
    handlers.unregister_handlers()
    operators.unregister_operators()
    preferences.unregister_preferences()
    properties.unregister_properties()
    task_queue.unregister_task_queue()
    ui_panels.unregister_ui_panels()
    ui_preset_styles.unregister_ui_preset_styles()


if __name__ == "__main__":
    register()
