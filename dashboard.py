import streamlit as st
import json

# JSON data
data = {
    "results": [
        {
            "test_case": "Redundant Class 1 (RotatingCatAnimator)",
            "result": {
                "redundant_code": True,
                "coverage_map": [0.9595],
                "best_coverage": 0.9595,
                "most_similar_class": "SpinningCatAnimator",
                "class_similarity_score": 0.9595,
                "snippet": """class RotatingCatAnimator(BaseAnimator):\n    def animate(self):\n        if not self.frame_manager:\n            return\n        cycle = 0\n        while cycle < self.repeat:\n            idx = 0\n            while idx < len(self.frame_manager):\n                self._clear_console()\n                print(Fore.YELLOW + f\"Cycle {cycle+1}/{self.repeat}, \" + Fore.CYAN + f\"Frame {idx+1}/{len(self.frame_manager)}\\n\")\n                print(Fore.GREEN + str(self.frame_manager.get_frames()[idx]))\n                time.sleep(self.delay)\n                idx += 1\n            cycle += 1\n""",
                "most_similar_class_code": """class SpinningCatAnimator(BaseAnimator):\n    def animate(self):\n        if len(self.frame_manager) == 0:\n            print(\"No frames to animate.\")\n            return\n        for cycle in range(self.repeat):\n            for idx, frame in enumerate(self.frame_manager.get_frames()):\n                self._clear_console()\n                cycle_str = Fore.YELLOW + f\"Cycle {cycle+1}/{self.repeat}\"\n                frame_str = Fore.CYAN + f\"Frame {idx+1}/{len(self.frame_manager)}\"\n                print(f\"{cycle_str}, {frame_str}\\n\")\n                print(Fore.GREEN + str(frame))\n                time.sleep(self.delay)\n"""
            }
        },
        {
            "test_case": "Redundant Class 2 (MirroredSpinningCatAnimator)",
            "result": {
                "redundant_code": True,
                "coverage_map": [0.9601],
                "best_coverage": 0.9601,
                "most_similar_class": "SpinningCatAnimator",
                "class_similarity_score": 0.9601,
                "snippet": """class MirroredSpinningCatAnimator(BaseAnimator):\n    def animate(self):\n        if not self.frame_manager:\n            return\n        for cycle in range(self.repeat):\n            frames = self.frame_manager.get_frames()\n            for idx in range(len(frames) * 2):  # Doubles frame count, mirrors the second half\n                self._clear_console()\n                frame = frames[idx % len(frames)]\n                print(Fore.YELLOW + f\"Cycle {cycle+1}/{self.repeat}, \" + Fore.CYAN + f\"Frame {idx+1}/{len(frames)*2}\\n\")\n                print(Fore.GREEN + (\"\\n\".join(line[::-1] for line in str(frame).split(\"\\n\")) if idx >= len(frames) else str(frame)))\n                time.sleep(self.delay)\n""",
                "most_similar_class_code": """class SpinningCatAnimator(BaseAnimator):\n    def animate(self):\n        if len(self.frame_manager) == 0:\n            print(\"No frames to animate.\")\n            return\n        for cycle in range(self.repeat):\n            for idx, frame in enumerate(self.frame_manager.get_frames()):\n                self._clear_console()\n                cycle_str = Fore.YELLOW + f\"Cycle {cycle+1}/{self.repeat}\"\n                frame_str = Fore.CYAN + f\"Frame {idx+1}/{len(self.frame_manager)}\"\n                print(f\"{cycle_str}, {frame_str}\\n\")\n                print(Fore.GREEN + str(frame))\n                time.sleep(self.delay)\n"""
            }
        },
        {
            "test_case": "Novel Class 1 (RainbowCatAnimator)",
            "result": {
                "redundant_code": False,
                "coverage_map": [0.8084, 0.5272, 0.4831, 0.8643],
                "best_coverage": 0.8643,
                "most_similar_class": "ShakySpinningCatAnimator",
                "class_similarity_score": 0.612,
                "snippet": """class RainbowCatAnimator(BaseAnimator):\n    def __init__(self, frame_manager, delay=0.4, repeat=1, clear_screen=True, rainbow_speed=0.3):\n        super().__init__(frame_manager, delay, repeat, clear_screen)\n        self.rainbow_speed = rainbow_speed\n        self.colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]\n\n    def _rainbow_text(self, text, frame_idx):\n        color_cycle = self.colors[frame_idx % len(self.colors)]\n        return "\\n".join(color_cycle + line for line in text.split("\\n"))\n\n    def _add_trail(self, text, frame_idx):\n        trail = "." * (frame_idx % 5)\n        return "\\n".join(line + trail for line in text.split("\\n"))\n\n    def animate(self):\n        if not self.frame_manager:\n            return\n        for cycle in range(self.repeat):\n            for idx, frame in enumerate(self.frame_manager.get_frames()):\n                self._clear_console()\n                print(Fore.YELLOW + f\"Rainbow Cycle {cycle+1}/{self.repeat}\")\n                print(Fore.CYAN + f\"Frame {idx+1}/{len(self.frame_manager)}\\n\")\n                styled_text = self._rainbow_text(str(frame), idx)\n                styled_text = self._add_trail(styled_text, idx)\n                print(styled_text)\n                time.sleep(self.rainbow_speed)\n""",
                "most_similar_class_code": """class ShakySpinningCatAnimator(BaseAnimator):\n    def __init__(self, frame_manager, delay=0.4, repeat=1, clear_screen=True, amplitude=2):\n        super().__init__(frame_manager, delay, repeat, clear_screen)\n        self.amplitude = amplitude\n\n    def _shake_lines(self, text):\n        lines = text.split("\\n")\n        new_lines = []\n        for ln in lines:\n            offset = random.randint(-self.amplitude, self.amplitude)\n            if offset > 0:\n                new_lines.append(" " * offset + ln)\n            else:\n                new_lines.append(ln)\n        return "\\n".join(new_lines)\n\n    def animate(self):\n        if len(self.frame_manager) == 0:\n            print("No frames to animate.")\n            return\n        for cycle in range(self.repeat):\n            for idx, frame in enumerate(self.frame_manager.get_frames()):\n                self._clear_console()\n                c_str = Fore.YELLOW + f\"Shaky Cycle {cycle+1}/{self.repeat}\"\n                f_str = Fore.CYAN + f\"Frame {idx+1}/{len(self.frame_manager)}\"\n                print(f"{c_str}, {f_str}\\n")\n                shaken = self._shake_lines(frame.ascii_art)\n                print(Fore.GREEN + shaken)\n                time.sleep(self.delay)\n"""
            }
        },
        {
            "test_case": "Novel Class 2 (ShadowCatAnimator)",
            "result": {
                "redundant_code": False,
                "coverage_map": [0.7648, 0.4189, 0.4662, 0.8968],
                "best_coverage": 0.8968,
                "most_similar_class": "ShakySpinningCatAnimator",
                "class_similarity_score": 0.5742
            }
        },
        {
            "test_case": "Redundant Method 1 (_shake_lines)",
            "result": {
                "redundant_code": True,
                "highest_similarity": 0.98,
                "most_similar_method": "def _shake_lines",
                "complementary_class": None
            }
        },
        {
            "test_case": "Redundant Method 2 (_flip_text)",
            "result": {
                "redundant_code": True,
                "highest_similarity": 0.9859,
                "most_similar_method": "def _flip_text",
                "complementary_class": None
            }
        },
        {
            "test_case": "Novel Method 1 (_invert_colors)",
            "result": {
                "redundant_code": False,
                "highest_similarity": 0.6539,
                "most_similar_method": "def _flip_text",
                "complementary_class": None
            }
        },
        {
            "test_case": "Novel Method 2 (_fade_out_effect)",
            "result": {
                "redundant_code": False,
                "highest_similarity": 0.5534,
                "most_similar_method": "def _shake_lines",
                "complementary_class": None
            }
        },
        {
            "test_case": "Novel Method 3",
            "result": {
                "redundant_code": False,
                "highest_similarity": 0.5303,
                "most_similar_method": "def _shake_lines",
                "complementary_class": "ShakySpinningCatAnimator"
            }
        }
    ]
}

# Streamlit Dashboard
st.set_page_config(page_title="Code Analysis Dashboard", layout="wide")
st.title("🔍 Code Analysis Dashboard")
st.markdown("""
    Welcome to the Code Analysis Dashboard! Here you can:
    - Explore similarity analysis for classes and methods.
    - Identify redundant code or discover novel additions.
    - Review complementary class suggestions for better organization.
""")

# Display results
for test in data["results"]:
    test_case = test["test_case"]
    result = test["result"]

    with st.expander(f"🔗 {test_case}", expanded=True):
        st.subheader(f"Analysis for {test_case}")

        # Display redundant status
        is_redundant = "✅ Yes" if result.get("redundant_code") else "❌ No"
        st.markdown(f"**Redundant Code:** {is_redundant}")

        # Display most similar class
        if "most_similar_class" in result and result["most_similar_class"]:
            st.markdown(f"**Most Similar Class:** `{result['most_similar_class']}`")

        # Display best coverage
        if "best_coverage" in result:
            st.markdown(f"**Best Coverage Score:** `{result['best_coverage']}`")

        # Display example snippet
        if "snippet" in result:
            st.markdown("### Input Code Snippet")
            st.code(result["snippet"], language="python")

        # Display most similar class code
        if "most_similar_class_code" in result:
            st.markdown("### Most Similar Class Code")
            st.code(result["most_similar_class_code"], language="python")

        # Display JSON summary
        st.markdown("### Detailed Results")
        st.json(result)

st.sidebar.title("Navigation")
st.sidebar.markdown("Use the main view to explore results in detail.")
st.sidebar.info("🔍 Insights powered by similarity analysis tools.")
