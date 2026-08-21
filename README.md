# Device Health Score

A lightweight diagnostic engine that evaluates device health based on battery level, network connectivity, storage availability, and GPS status.

## Features

- Health score calculation (0-100)
- Letter grade classification (A-F)
- Device risk assessment
- Device status detection
- Automatic issue identification
- Actionable recommendations
- Timestamped reports

---

## Health Metrics

The engine evaluates device health using the following indicators:

- Battery percentage
- Network availability
- Available storage space
- GPS status

Each detected issue reduces the overall health score.

---

## Scoring Logic

The health score starts at **100 points** and is reduced based on detected conditions.

| Condition | Penalty |
|------------|----------|
| Critical battery level (<10%) | -30 |
| Low battery level (<20%) | -15 |
| Network unavailable | -20 |
| Critical storage space (<2 GB) | -25 |
| Low storage space (<5 GB) | -10 |
| GPS disabled | -10 |

---

## Status Levels

Based on the final score, the device receives a status.

| Score Range | Status |
|-------------|--------|
| 90-100 | HEALTHY |
| 70-89 | WARNING |
| 0-69 | CRITICAL |

---

## Health Grade Classification

The score is also converted to a letter grade.

| Score Range | Grade |
|-------------|--------|
| 90-100 | A |
| 80-89 | B |
| 70-79 | C |
| 60-69 | D |
| Below 60 | F |

---

## Device Risk Level

The engine determines operational risk based on the health score.

| Score Range | Risk Level |
|-------------|-------------|
| 90-100 | LOW |
| 70-89 | MEDIUM |
| 50-69 | HIGH |
| Below 50 | CRITICAL |

### Example

```json
{
  "health_score": 82,
  "health_grade": "B",
  "risk_level": "MEDIUM",
  "status": "WARNING"
}
```

The risk level helps prioritize remediation efforts and quickly identify devices that require immediate attention.

---

## Recommendations Engine

Detected issues are automatically mapped to actionable recommendations.

### Examples

| Issue | Recommendation |
|---------|---------------|
| Critical battery level | Charge the device immediately |
| Low battery level | Consider charging the device soon |
| Network unavailable | Verify Wi-Fi or cellular connection |
| Critical storage space | Remove unnecessary files |
| Low storage space | Free additional storage space |
| GPS disabled | Enable location services |

---

## Sample Output

```json
{
  "timestamp": "2026-08-21T10:15:30",
  "health_score": 65,
  "health_grade": "D",
  "risk_level": "HIGH",
  "status": "CRITICAL",
  "issues": [
    "Low battery level",
    "Low storage space",
    "GPS disabled"
  ],
  "recommendations": [
    "Consider charging the device soon.",
    "Free additional storage space.",
    "Enable location services."
  ]
}
```

---

## Example Usage

```python
from health_score import DeviceState, calculate_health_score

device = DeviceState(
    battery_percent=18,
    network_available=True,
    free_storage_gb=3.5,
    gps_enabled=False
)

result = calculate_health_score(device)

print(result)
```

---

## Future Improvements

Planned enhancements:

- Historical trend analysis
- CSV export
- HTML report generation
- YAML-based configuration
- Dashboard visualization
- GitHub Actions integration
- Multi-device comparison
- Health score analytics

---

## License

MIT License
