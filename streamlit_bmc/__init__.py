import os
import streamlit.components.v1 as components

# Create a _RELEASE constant. We'll set this to False while we're developing
# the component, and True when we're ready to package and distribute it.
# (This is, of course, optional - there are innumerable ways to manage your
# release process.)
_RELEASE = False

# Declare a Streamlit component. `declare_component` returns a function
# that is used to create instances of the component. We're naming this
# function "_component_func", with an underscore prefix, because we don't want
# to expose it directly to users. Instead, we will create a custom wrapper
# function, below, that will serve as our component's public API.

# It's worth noting that this call to `declare_component` is the
# *only thing* you need to do to create the binding between Streamlit and
# your component frontend. Everything else we do in this file is simply a
# best practice.

if not _RELEASE:
    _component_func = components.declare_component(
        # We give the component a simple, descriptive name ("streamlit_bmc"
        # does not fit this bill, so please choose something better for your
        # own component :)
        "streamlit_bmc",
        # Pass `url` here to tell Streamlit that the component will be served
        # by the local dev server that you run via `npm run start`.
        # (This is useful while your component is in development.)
        url="http://localhost:3001",
    )
else:
    # When we're distributing a production version of the component, we'll
    # replace the `url` param with `path`, and point it to to the component's
    # build directory:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/public")
    _component_func = components.declare_component("streamlit_bmc", path=build_dir)


# Create a wrapper function for the component. This is an optional
# best practice - we could simply expose the component function returned by
# `declare_component` and call it done. The wrapper allows us to customize
# our component's API: we can pre-process its input args, post-process its
# output value, and add a docstring for users.
def st_bmc(data, key=None):
    """Create a new instance of "business_model_canvas".

    Parameters
    ----------
    data: json
        The name of the thing we're saying hello to. The component will display
        the text "Hello, {name}!"
    key: str or None
        An optional key that uniquely identifies this component. If this is
        None, and the component's arguments are changed, the component will
        be re-mounted in the Streamlit frontend and lose its current state.

    Returns
    -------
    void
        Simple is golden

    """
    # Call through to our private component function. Arguments we pass here
    # will be sent to the frontend, where they'll be available in an "args"
    # dictionary.
    #
    # "default" is a special argument that specifies the initial return
    # value of the component before the user has interacted with it.
    component_value = _component_func(data=data, key=key, default=0)

    # We could modify the value returned from the component if we wanted.
    # There's no need to do this in our simple example - but it's an option.
    return component_value


# Add some test code to play with the component while it's in development.
# During development, we can run this just as we would any other Streamlit
# app: `$ streamlit run streamlit_bmc/__init__.py`
if not _RELEASE:
    import streamlit as st
    # Create an instance of our component with a constant `data` arg, and
    # print its output value.
    st.set_page_config(
        page_title="Ex-stream-ly Cool App",
        page_icon="🧊",
        layout="wide",
        initial_sidebar_state="expanded",
        menu_items={
            'Get Help': 'https://www.extremelycoolapp.com/help',
            'Report a bug': "https://www.extremelycoolapp.com/bug",
            'About': "# This is a header. This is an *extremely* cool app!"
        }
    )
    data = {
        "visual": {
            "company_name": "Apple"
        },
        "key_partners": {
            "cards": [
                { "id":"1", "text": "Manufacturing Partners (mostly chinese)" },
                { "id":"2", "text": "Cellphone Carriers" }
            ]
        },
        "key_activities": {
            "cards": [
                { "id":"1", "text": "New Product Development" },
                { "id":"2", "text": "Marketing" }
            ]
        },
        "key_resources": {
            "cards": [
                { "id":"1", "text": "Intelectual Property (Operational Systems, digital plataform, etc)" },
                { "id":"2", "text": "Brand" }
            ]
        },
        "value_propositions": {
            "cards": [
                { "id":"1", "text": "Premium High-End Products and Experience" },
                { "id":"2", "text": "An ecosystem of interconnected services" },
                { "id":"3", "text": "Access to iPhone/iPad user base" }
            ]
        },
        "customer_relationship": {
            "cards": [
                { "id":"1", "text": "Love Brand" },
                { "id":"2", "text": "Apple Care" }
            ]
        },
        "channels": {
            "cards": [
                { "id":"1", "text": "Apple Stores" },
                { "id":"2", "text": "App Store / iTunes" }
            ]
        },
        "customer_segments": {
            "cards": [
                { "id":"1", "text": "Product Buyers" },
                { "id":"2", "text": "Service Subscribers" },
                { "id":"3", "text": "App Developers + Music & Video Producers" }
            ]
        },
        "cost_structure": {
            "cards": [
                { "id":"1", "text": "Operational Costs" },
                { "id":"2", "text": "Marketing and Branding" }
            ]
        },
        "revenue_streams": {
            "cards": [
                { "id":"1", "text": "Product Sales (High-Priced Tech)" },
                { "id":"2", "text": "Service Subscriptions (Recurring Revenue)" },
                { "id":"3", "text": "App and Media Revenues (30% cut)" }
            ]
        }
    }
    with st.container():
        # You can call any Streamlit command, including custom components:
        st_bmc(data)
