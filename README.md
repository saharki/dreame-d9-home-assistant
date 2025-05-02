# Dreame Vacuum D9 Home Assistant Integration

Integrate your Dreame robot vacuum (e.g., D9) with Home Assistant over your local network using the `python-miio` library.

## Features

- Start, stop, and return the vacuum to base
- Status reporting
- UI-based configuration (via Home Assistant config flow)
- HACS compatible

## Installation

1. **HACS (Recommended):**
   - Add this repository as a custom repository in HACS.
   - Install the `Dreame Vacuum` integration from HACS.
2. **Manual:**
   - Copy the `dreame_vacuum` folder to your Home Assistant `custom_components` directory.

## Requirements

- Home Assistant 2022.0.0 or newer
- `python-miio` (installed automatically)

## Configuration

1. Restart Home Assistant after installation.
2. Go to **Settings > Devices & Services > Add Integration** and search for "Dreame Vacuum".
3. Enter your vacuum's IP address and token in the setup dialog.

## Usage

- The vacuum will appear as a device in Home Assistant.
- You can start, stop, and return to base from the UI or automations.

## Troubleshooting

- Ensure your vacuum is on the same network as Home Assistant.
- You may need to extract the token using tools like [python-miio](https://github.com/rytilahti/python-miio) or Mi Home app.

## Links

- [GitHub Repository](https://github.com/saharki/dreame-d9-home-assistant)
- [python-miio Documentation](https://python-miio.readthedocs.io/)

---

This project is not affiliated with Dreame or Xiaomi.
