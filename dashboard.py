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
                "class_similarity_score": 0.9595
            }
        },
        {
            "test_case": "Redundant Class 2 (MirroredSpinningCatAnimator)",
            "result": {
                "redundant_code": True,
                "coverage_map": [0.9601],
                "best_coverage": 0.9601,
                "most_similar_class": "SpinningCatAnimator",
                "class_similarity_score": 0.9601
            }
        },
        {
            "test_case": "Novel Class 1 (RainbowCatAnimator)",
            "result": {
                "redundant_code": False,
                "coverage_map": [0.8084, 0.5272, 0.4831, 0.8643],
                "best_coverage": 0.8643,
                "most_similar_class": "ShakySpinningCatAnimator",
                "class_similarity_score": 0.612
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

        # Display complementary class
        if "complementary_class" in result and result["complementary_class"]:
            st.markdown(f"**Complementary Class:** `{result['complementary_class']}`")

        # Display best coverage
        if "best_coverage" in result:
            st.markdown(f"**Best Coverage Score:** `{result['best_coverage']}`")

        # Display JSON summary
        st.markdown("### Detailed Results")
        st.json(result)

        # Example Code Snippet
        if "test_case" in test_case.lower():
            st.markdown("### Example Code Snippet")
            st.code("""
def example_function():
    print("This is an example")
""", language="python")

st.sidebar.title("Navigation")
st.sidebar.markdown("Use the main view to explore results in detail.")
st.sidebar.info("🔍 Insights powered by similarity analysis tools.")
