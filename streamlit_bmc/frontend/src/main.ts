import { WithStreamlitConnection } from "./streamlit";
import BMCComponent from "./BMCComponent.svelte";

// "WithStreamlitConnection" is a wrapper component. It bootstraps the
// connection between your component and the Streamlit app, and handles
// passing arguments from Python -> Component.
//
// You don't need to edit withStreamlitConnection (but you're welcome to!).
const bmcComponent = new WithStreamlitConnection({
  target: document.body,
  props: {
    /**
     * Custom Streamlit component
     */
    component: BMCComponent,

    /**
     * Set to false if you want `args` (the named dictionary of arguments passed
     * from Python) to be passed as a dictionary to your component.
     *
     * Default is `true`.
     */
    spreadArgs: true,
  },
});

export default bmcComponent;
