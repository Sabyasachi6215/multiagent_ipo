import os
import streamlit as st
from crewai import Agent, Task, Crew, LLM
from crewai_tools import SerperDevTool
from dotenv import load_dotenv
from crewai_tools import YoutubeChannelSearchTool
from crewai_tools import YoutubeVideoSearchTool



# Load environment variables
load_dotenv()

# Streamlit page config
st.set_page_config(page_title="IPO Analysis & Market Research", page_icon="📰", layout="wide")


# Title and description
st.title("🤖 IPO Analysis & Market Research")


# Sidebar
with st.sidebar:
    st.header("Content Settings")
    
    # Make the text input take up more space
    topic = st.text_area(
        "Enter the IPO name",
        height=100,
        placeholder="Enter the IPO name  you want to generate analysis about..."
    )
    
    # # Add more sidebar controls if needed
    # st.markdown("### Advanced Settings")
    # temperature = st.slider("Temperature", 0.0, 1.0, 0.7)
    
    # Add some spacing
    st.markdown("---")
    
    # Make the generate button more prominent in the sidebar
    generate_button = st.button("Generate Content", type="primary", use_container_width=True)

    if "channel" not in st.session_state:
     
     st.session_state["channel"] = ""

    channel = st.text_input(
        "Enter YouTube channel link",
        value=st.session_state["channel"],
        placeholder="Type the channel name"
    )


    # channel = st.text_input("Enter YouTube channel link", placeholder="Type the channel name")

    generate_Youtube_analysis = st.button("Generate Analysis from YouTube Video", type="primary", use_container_width=True)
    
    # Add some helpful information
    with st.expander("ℹ️ How to use"):
        st.markdown("""
        1. Enter your desired topic in the text area above
        2. Adjust the temperature if needed (higher = more creative)
        3. Click 'Generate Content' to start
        4. Wait for the AI to generate your article
        5. Download the result as a markdown file
        """)

def generate_content(topic):
    llm = LLM(
        model="command-r",
        temperature=0.1
    )

    search_tool = SerperDevTool(n_results=10)
    

    # First Agent: Senior Research Analyst
    senior_research_analyst = Agent(
        role="Senior Market Research Analyst",
        goal=f"Research, analyze, and synthesize comprehensive information on {topic} from reliable web sources",
        backstory="You're an expert Indian Stock market research analyst with advanced web research skills. "
                "For New IPO in Indian market, you are able to understand the market sentiment"
                "Check crucial factors for IPO like estimated listing gains"
                "You excel at finding, analyzing, and synthesizing information from "
                "across the internet using search tools. You're skilled at "
                "distinguishing reliable sources from unreliable ones, "
                "fact-checking, cross-referencing information, and "
                "identifying key patterns and insights. You provide "
                "well-organized research briefs with proper citations "
                "and source verification. Your analysis includes both "
                "raw data and interpreted insights, making complex "
                "information accessible and actionable.",
        allow_delegation=False,
        verbose=True,
        tools=[search_tool],
        llm=llm
    )

    # Second Agent: Content Writer
    content_writer = Agent(
        role="Content Writer",
        goal="Transform research findings into engaging blog posts and sentiment analysis of the market while maintaining accuracy",
        backstory="You're a skilled content writer specialized in creating "
                "engaging, accessible content from technical research. "
                "You work closely with the Senior Research Analyst and excel at maintaining the perfect "
                "balance between informative and entertaining writing, "
                "while ensuring all facts and citations from the research "
                "are properly incorporated. You have a talent for making "
                "complex topics approachable without oversimplifying them.",
        allow_delegation=False,
        verbose=True,
        llm=llm
    )

    # Research Task
    research_task = Task(
        description=("""
            1. Conduct comprehensive research on {topic} including:
                - Recent developments and news
                - Key industry trends and innovations
                - Expert opinions and analyses
                - Statistical data and market insights
            2. Evaluate source credibility and fact-check all information
            3. Organize findings into a structured research brief
            4. Include all relevant citations and sources
        """),
        expected_output="""A detailed research report containing:
            - Executive summary of key findings
            - Market sentiment analysis of the new IPO in the Indian share market
            - should analyse Estimated listing gains of the company
            - Information about the IPO objective and why the company is raising funds
            - Comprehensive analysis of current trends and developments
            - List of verified facts and statistics
            - All citations and links to original sources
            - Clear categorization of main themes and patterns
            Please format with clear sections and bullet points for easy reference.""",
        agent=senior_research_analyst
    )

    # Writing Task
    writing_task = Task(
        description=("""
            Using the research brief provided, create an engaging blog post that:
            1. Transforms technical information into accessible content
            2. Maintains all factual accuracy and citations from the research
            3. Includes:
                - Attention-grabbing introduction
                - Well-structured body sections with clear headings
                - Compelling conclusion
            4. Preserves all source citations in [Source: URL] format
            5. Includes a References section at the end
        """),
        expected_output="""A polished blog post in markdown format that:
            - New IPO recommendation, Should the investor buy it or not
            - Should give 5 pointers each on Strengths and Risk about the Stock.
            - Should give information about yearwise Revenue , Profit and Total Assests of the company
            - Reports should have Estimated listing gains of the company
            - Reports should indicate information about the IPO objective and why the company is raising funds
            - Engages readers while maintaining accuracy
            - Contains properly structured sections
            - Includes Inline citations hyperlinked to the original source url
            - Presents information in an accessible yet informative way
            - Follows proper markdown formatting, use H1 for the title and H3 for the sub-sections""",
        agent=content_writer
    )

    # Create Crew
    crew = Crew(
        agents=[senior_research_analyst, content_writer],
        tasks=[research_task, writing_task],
        verbose=True
    )

    return crew.kickoff(inputs={"topic": topic})


def generate_youtube_analysis(topic):
    llm = LLM(
        model="command-r",
        temperature=0.1
    )

    yt_tool = YoutubeChannelSearchTool(youtube_channel_handle=channel)

    # First Agent: Senior Research Analyst
    blog_reseracher = Agent(   
        role='Senior Share market Reseracher',
        goal='get the relevant video content for the topic {topic} from Youtube Channel',                   
        verbose=True,
        memory=True,
        backstory='Expert in understanding share market and IPO reletd contents from Youtube Channel',
        llm=llm,
        tools =[yt_tool],
        allow_delegation=True
)

    # Second Agent: Content Writer
    blog_writer=Agent(

        role='Writer',
        goal='Narrate compelling tech stories about the video {topic} from YT channel',                   
        verbose=True,
        memory=True,
        backstory=(
        "With aflair for Simplifying complex topics, you craft"
        "engaging narratives that captivate and educate, bringing new"
        "discoveries to light in a accessible manner."),
        llm=llm,
        tools =[yt_tool],
        allow_delegation=False
)

    # Research Task
    research_task=Task(

    description=("Identify the video {topic}."
             
                 "Get detailed information about the video from the channel."),

    expected_output='A comprehensive 3 paragrpah long report based on the {topic} of video content.',

    tools =[yt_tool],
    agent=blog_reseracher,

)

    # Writing Task
    writing_task=Task(

    description=("get the info from the youtube channel on topic {topic}."),

    expected_output='Summarize the info from the youtube channel video on the topic {topic} and create the content for the blog post',

    tools =[yt_tool],
    agent=blog_writer,
    async_execution=False,
    output_file='new-blog-IPO_1.md'
)

    # Create Crew
    crew = Crew(
        agents=[blog_reseracher, blog_writer],
        tasks=[research_task, writing_task],
        verbose=True
    )

    return crew.kickoff(inputs={"topic": topic})

# Main content area
if generate_button:
    with st.spinner('Generating content... This may take a moment.'):
        try:
            result = generate_content(topic)
            st.markdown("### Generated Content")
            st.markdown(result)
            
            # # Add download button
            # st.download_button(
            #     label="Download Content",
            #     data=result.raw,
            #     file_name=f"{topic.lower().replace(' ', '_')}_article.md",
            #     mime="text/markdown"
            # )
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

if generate_Youtube_analysis:
    with st.spinner('Generating content from Youtube... This may take a moment.'):
        try:
            result = generate_youtube_analysis(topic)
            st.markdown("### Generated Content")
            st.markdown(result)
            
            # Add download button
            # st.download_button(
            #     label="Download Content",
            #     data=result.raw,
            #     file_name=f"{topic.lower().replace(' ', '_')}_article.md",
            #     mime="text/markdown"
            # )
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

# Footer
st.markdown("---")
st.markdown("Built with CrewAI, Streamlit and powered by Cohere's Command R7B")