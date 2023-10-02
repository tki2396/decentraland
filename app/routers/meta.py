from fastapi import HTTPException, APIRouter

from app.models.domain_models import Nodeinfo, NodeinfoWellKnown, WebfingerLink, WebfingerResponse

router = APIRouter()

@router.get("/.well-known/webfinger")
async def webfinger(subject: str):
    # Example: subject = "acct:username@domain.com"
    
    # Split and validate the subject
    if not subject.startswith("acct:"):
        raise HTTPException(status_code=400, detail="Invalid resource")
    
    username = subject.split("acct:")[1].split("@")[0]
    
    # Check if user exists (replace this with your DB check)
    if username not in ["some_known_username"]: 
        raise HTTPException(status_code=404, detail="User not found")

    # Construct the Webfinger response
    response = WebfingerResponse(
        subject=subject,
        aliases=[f"https://yourdomain.com/@{username}"], 
        links=[
            WebfingerLink(
                rel="self",
                type="application/activity+json",
                href=f"https://yourdomain.com/users/{username}"
            ),
            # Add other links as needed, e.g., to the user's inbox, outbox, etc.
        ]
    )
    return response

@router.get("/.well-known/nodeinfo")
async def well_known_nodeinfo():
    response = NodeinfoWellKnown(
        links=[
            {
                "rel": "http://nodeinfo.diaspora.software/ns/schema/2.0",
                "href": "https://yourdomain.com/nodeinfo/2.0"
            },
            # Other versions or URLs if necessary
        ]
    )
    return response


@router.get("/nodeinfo/2.0")
async def nodeinfo_v2_0():
    response = Nodeinfo(
        version="2.0",
        software={
            "name": "your_software_name",
            "version": "your_software_version"
        },
        protocols=["activitypub"],
        services={
            "inbound": [],
            "outbound": ["rss", "atom"]
        },
        openRegistrations=True,
        usage={
            "users": {
                "total": 100, # Replace with your actual user count
                "activeHalfyear": 50, # Users active in the last 6 months
                "activeMonth": 30 # Users active in the last month
            },
            # Other usage stats if available
        }
        # ... other fields you want to expose
    )
    return response

