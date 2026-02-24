# GM01701: React Native

@ George Madeley
@ Personal Studies
@ 3/15/24

## Introduction

This is a collection of notes that I, George Madeley, took when taking the Codecademy React Native course. I do not take ownership of the material covered and these notes should only be used for educational purposes

### Contents

[Introduction](#introduction)

[Contents](#contents)

[Section 1: React Native](#react-native)

[1 - Introduction to React Native](#introduction-to-react-native)

[2 - Core Components](#core-components)

[3 - Styling Components](#styling-components)

[4 - Navigation](#navigation)

## React Native

### Introduction to React Native

#### What is React Native?

React Native is a library built with the same API as React. Without Expo or React Native, pure native app development would require you to learn the platform language and tooling like Android Studio for Android and Xcode iOS.

#### Expo and React Native

Expo is a platform to make universal React apps that helps your develop, build, deploy, and quickly iterate on mobile apps.

- Expo Go is an app you can download on your phone to "view" your app in development.
- Expo CLI is a tool to create, manage, ad develop your apps.
- Expo SDK is a modular set of packages that provide access to native APIs, like _Camera_ or _Notifications_.
- Expo Snack is a web-based playground where you can write React Native snippets and run them in the browser.

Expo is not a requirement but is highly recommended.

#### Render a Component

All apps in Expo and React Native are made from components. These components are small reusable pieces of your app, all working together. Just like in React, your app descends from a single component. Instead of rendering this to the DOM, Expo and React Native renders it for your using a concept called the entry point.

#### Native Rendering

In React, you have access to HTML components, in React Native, you have access to core components. React Native knows how to render these on a specific platform because they are tied to a native component counterpart. The JavaScript with the components is bundled in your app and executed in a separate thread from the native UI. This JS thread instructs React Native what it needs to render. Splitting this into a JS thread and a UI thread allows the platform to understand what needs to be rendered without blocking the actual interface components.

Besides the visible UI components, the native UI thread is also handling native API requests. Some functionality, like GPS location, needs to be requested from the native APIs. If your JS code uses this kind of functionality, it interacts with the native API using native code. The data from this native code is sent back to the JS code and handled in your app.

#### Cross-Platform Differences

Native components may look different because of the platform-provided design guidelines. On iOS, Apple implemented their Human Interface guidelines while Android provides their Material Design guidelines. Some of the core components might look different on other platforms because of this.

#### Creating an Expo App

To create the app, you'll first need a few things installed on your computer:

- Node.js -- A JavaScript runtime,
- Visual Studio Code -- A text editor

There are also few helpful commands line commands:

- `node -v` - checks your version of Node.js
- `npm -v` - checks your version of Node package manager
- `npm install -g expo-cli` - installs the Expo command-line tools.
- `expo init hello-word` - creates a new expo app named "hello-world".

#### Testing the App with Expo Go

To test the app on your mobile device, you'll need to download and install the Expo Go app. The Expo Go app will sync with the Expo command-line tools.

Once you have the Expo Go app installed, you can run the app using the `npm start` command. You then open the Expo Go app and scan the QR code which should have popped up in the terminal. Anytime you make changes to the app, it will automatically update on your mobile device.

### Core Components

#### What is a core component?

In Expo and React Native, components are translated to native components for the platform it's running on. React Native provides a set of ready-to-use components is called "core components" and most of them have built-in Android and iOS implementations.

You can import these components from the `react-native` package.

#### View Component

With View, you can create responsive layouts using flex-box or add basic styling to nested components. The component is best comparable with a div HTML element.

```jsx
<View style={{ width: 250, backgroundColor: "yellow" }}>...</View>
```

All components are flex-box by default.

#### Text component

To render text on Android and iOS, the string needs to be wrapped in a Text component.

#### Image component

The Image component is very similar to the img HTML element. One of the additional features of `<Image>` is the ability to load images from different sources. This could be a publicly accessible link, local file reference, Base64-encoded string, or image imported as module with require.

React Native uses the source property to instruct an Image component what to display. We must define the source as a JavaScript object containing the uri property.

```jsx
<Image
  source={{
    uri: "https://example.com/cool-image.jpg",
  }}
/>
```

#### ScrollView component

View components aren't scrollable in Expo and React Native. Rendering scrollable content requires additional calculations which could hurt performance when applied to all View components. Expo and React Native have different scrollable components that we can use, like ScrollView. ScrollView allows us to fully manage and customize how the content should be scrolled.

#### Button component

We can use a Button component for user interactions. To capture the user clicking the button, we need to use the onPress event handler. This property is required for the Button component.

```jsx
<Button title="Profile page" onPress={() => navigate("profile")} />
```

All components are pressable, so you do not have to use a button.

The Pressable component is an adequate alternative to the Button component as it contains the functionality of a button, but it doesn't include how the button is rendered. A cool feature from Pressable is that it informs the child elements if the Pressable is currently pressed or not. This only works when using a method as a child in the Pressable component.

```jsx
<Pressable>{(state) => <Box pressed={state.pressed} />}</Pressable>
```

#### TestInput component

The TestInput component is created to capture textual and numeric input. This component is best comparable with the `<input>` HTML element. To listen to input changes from the user, we can use the onChangeText event handler. This event handler receives the input as a string, provided by the user.

You can add the `secureTextEntry` property to hide the text like in password fields.

#### Accessibility properties

Both Android and iOS have built-in assistive functionality, like `TalkBack` or `VoiceOver`. These tools, also known as accessibility readers, read an app's contents out loud to users. In React Native, we can add textual descriptions without displaying the text. This helps accessibility readers communicate the action that will be performed when pressing the button. We can do that by defining the accessibility properties.

```jsx
<TouchableOpacity
  onPress={deleteItem}
  accessible={true}
  accessibilityLabel="Press to delete"
  accessibilityHint="The item will be deleted permanently"
>
  <TrashIcon />
</TouchableOpacity>
```

- **Accessible**: This property tells React Native to group the content into a single selectable component. When users tap the button, Android and iOS will select everything from the touchable opacity.
- **accessibilityLabel**: This describes how users can use the button. Accessibility readers will tell the user to "Press to delete".
- **accessibilityHint**: This optional description tells users what will happen after pressing the button.

These properties enable accessibility readers to describe the action when pressing the button. Without the text displayed, it will read out "Press to delete, the item will be deleted permanently" when accessibility users are trying to understand the button.

### Styling Components

#### Styling in Expo and React Native

One website, styling is typically done with CSS. But not everything from the web is available in Expo and React Native. To use React code and run them in a native environment, Expo and React Native uses a JavaScript thread. Since we are tied to JavaScript, we must define our styling in JavaScript too.

```jsx
<View
  style={{
    width: 100,
    height: 100,
    backgroundColor: "red",
  }}
/>
```

The style property is like inline styling in HTML elements. Instead of CSS rules, we must write everything in JavaScript. The properties that you must use are named after the CSS properties, only using camelCasing.

#### StyleSheets

When more styling rules are added, the readability of the code will degrade. This is one of the reasons why React Native created the StyleSheet API. With the StyleSheet API we can write our styling rules separately, and reference them when rendering the components.

```jsx
// Using the StyleSheet API
const AwesomeBox = () => <View style={styles.box} />;

const styles = StyleSheet.create({
  box: {
    width: 100,
    height: 100,
    backgroundColor: "red",
  },
});
```

The most important method of the StyleSheet API is the `.create` method. With that, we can create a nested object with styling rules and refer to the styling rules.

Some styling properties require objects instead of plain numbers or strings. `shadowOffset` is one of these properties: it requires an object with width and height. When adding new rules, it's recommended to check the required value in the documentation.

One of the biggest downsides of the StyleSheet API is that our styles are static. We can't change the styling based on user interaction from our `StyleSheet.create` method.

#### Combining Styles

The style property also accepts an array of inline style objects or StyleSheet references. It is similar to applying multiple CSS classes to a HTML element, e.g., `<div class="box red">`. Using this array with conditionally added styles, we can make the styling dynamic based on user interaction.

```jsx
const AwesomeBox = (props) => (
  <View style={[styles.box, props.isActive && { backgroundColor: "purple" }]} />
);

const styles = StyleSheet.create({
  box: {
    width: 100,
    height: 100,
    backgroundColor: "red",
  },
});
```

#### Width and Height

In mobile development it's common to use a different type of unit called Density Independent Pixels or `dp`. The `dp` unit takes the screen precision into account when setting the actual number of pixels. Don't worry though, you can still use percentages.

#### Flex (box)

The best way to make your layout responsive is by using Flex-box. It's like the web variant, with some minor differences:

- All elements are flex-boxes; you don't have to specify `display: flex`.
- Some default values are changed to better suit mobile apps.

By adding the flex property with a factor number, we tell React Native to distribute the available space by the factor provided.

#### Flex Direction

There are two different directions in which we can render the child elements -- horizontally row or vertically column.

- `row` renders child elements from left to right.
- `row-reverse` renders child elements from right to left.
- `column` renders child elements from top to bottom.
- `column-reverse` renders child elements from bottom to top.

#### Flex Justify Content

Flex-box also allows us to control how the child elements are positioned within our parent flex-box. The property to control this aspect is the justifyContent property. There are multiple values you can use:

- `center` renders child elements within the center of our parent flex-box.
- `flex-start` renders child elements at the start of our parent flex-box.
- `flex-end` renders child elements at the end of our parent flex-box.
- `space-around` renders child elements with reaming space around these elements.
- `space-between` renders child elements with remaining space between the elements, without space the start or end.
- `space-evenly` renders child elements with remaining space evenly divided. Including space at the start and end.

### Navigation

#### Navigation Patterns

The following are some commonly used navigation patterns:

- **Tab Navigation --** This pattern uses a tab bar to allow users to switch between screens. Usually, these screens contain different functionality, like home screen and a profile screen. There are more variants of the tab navigator, like Instagram's, TikTok's, and Facebook's. The tabs usually contain the primary functionality of an app, like a feed and profile screen.
- **Stack Navigation --** Instead of using a menu or tab bar, the user must go from screen to screen to navigate through all screens. When a user navigates from one screen to another, the screen is pushed on a stack. The order of the stack doesn't matter; every transition is another screen in the stack. However, when going back a page, the last screen is removed from the stack and the previous screen is displayed. These stacks usually contain screens that are functional related to each other, like a list of tasks and a task detail screen. Examples are Apples iOS settings app.
- **Drawer Navigation --** instead of using a tab bar, it uses a pane that can be opened by either swiping or opening a menu button. In this pane, there is a menu where the users can switch between screens. Like the tab bar pattern, these screens often contain the primary functionality of your app. Examples are the Discord app.

#### React Navigation

One of the core principles of `react-navigation` is the navigator. It's the fundamental structure that holds multiple screens of your app. The determines what screen should render and how transitions between multiple screens are animated. All the screens are identified and referred to by a unique name.

`react-navigation` ships with a couple of different navigators, each following one of the navigations patterns from earlier.

The `NavigationContainer` component is responsible for managing the app's navigation state and makes sure the navigators in your app can function. One must wrap the current App children with the `NavigationContainer` from `@react-navigation/native`.

Navigators in `react-navigation` are created by a factory method. The stack navigator is created by the `createStackNavigator`. This method returns an object with a Navigator and Screen property. These properties are unique components that you must use when rendering the screens.

```jsx
const Stack = createStackNavigator();

<Stack.Navigator>
  <Stack.Screen name="MyScreen" component={MyScreen} />
</Stack.Navigator>;
```

#### Tab Navigation

There are different types of tab navigators. Apples likes using a bottom one whilst Google likes either a bottom or top tab navigator but has different guidelines for each. To create a tab navigator, we use the following command: `createBottomTabNavigator` from the `@react-navigation/bottom-tabs` library. This method will also return an object with a Navigator and Screen component.

```jsx
const Tab = createBottomTabNavigator();

export const AppNavigator = () => (
  <Tab.Navigator>
    <Tab.Screen name="Feed" component={FeedScreen} />
    <Tab.Screen name="Catalog" component={CatalogScreen} />
  </Tab.Navigator>
);
```

#### Programmatic Navigation

We can code when we want to navigate the user to another screen. Every screen receives a `navigation` property. This property is an object with a lot of useful methods, like `.navigation('ScreenName')` or `.goBack()`.

```jsx
// Using properties, only available in screen components
const FeedScreen = (props) => {
  const nav = props.navigation;

  return <Button title="Go to home" onPress={() => nav.navigate("Home")} />;
};
```

You can also access this navigation object using the useNavigation hook.

```jsx
// Using the hook, available in all components
const HomeButton = () => {
  const nav = useNavigation();

  return <Button title="Go to home" onPress={() => nav.navigate("Home")} />;
};
```

#### Nested Navigation

When creating your app's navigational structure, you often need to use a combination of multiple different navigators. But be careful as things can get messy in both UI and in code.
