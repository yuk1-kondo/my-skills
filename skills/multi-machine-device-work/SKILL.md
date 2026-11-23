---
name: multi-machine-device-work
description: "Pin down which machine, which physical device and which location a hardware or remote task involves before running any command, so work starts on the right host the first time."
---

# Work Across the User's Machines and Devices

## Pin down where everything is

- Build a short location map at the start of any task that touches a remote machine or a physical device, covering the target host, where that host is, where the device is plugged in or kept, and where the user is right now.

- Pull the map from memory and the current conversation first, and ask the user one short question only for the entries that are missing or could have changed.

- Treat a device being connected as a claim about one specific host, and never let it stand in for a different machine the user also owns.

- Restate the map back in one line before the first command, so a wrong assumption surfaces before any work runs.

## Verify the host before acting

- Confirm the host you actually reached by checking its hostname or tailnet name at the start of every remote session, and compare it with the map before running anything else.

- Check for the device on that same host, for example by listing its serial or USB device entries, before concluding the device, cable or driver is at fault.

- Stop and recheck the map when a path, folder or device is missing, because a missing path on the wrong machine looks identical to a broken setup on the right one.

- Give the user commands that name the machine they must run them on, and say what output proves they ran on the right one.

## Hand off between machines

- State plainly when a step has to move to another machine, naming the reason in terms of where the device or the user physically is.

- Carry the confirmed state across the move, including which files are current, which build last passed and what was already tried, so the new host does not repeat finished work.

- Ask the user to perform on-device steps such as entering a token or holding a button only once the correct host is confirmed reachable and the device is confirmed visible on it.

## Report the location state

- Report progress with the host and device location attached, so the user can spot a mismatch from the report alone.

- Name the exact blocker when work cannot proceed, such as the device being at another location, instead of reporting a generic connection failure.

- Update memory with any durable location fact the task established, such as a device that now lives somewhere new, once the user confirms it.

## Available connectors

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

## Alternatives for better results

- Prefer a harmless read on the target host, such as a hostname or device listing, over a long diagnostic run whenever location is still uncertain.

- Batch every step that needs the user standing at a device into one visit, rather than asking for several trips to the same machine.
